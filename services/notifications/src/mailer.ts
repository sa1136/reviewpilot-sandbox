import { SESv2Client, SendEmailCommand } from "@aws-sdk/client-sesv2";

export interface Mail {
  to: string;
  template: string;
  data: Record<string, unknown>;
}

export interface Mailer {
  send(mail: Mail): Promise<void>;
}

export class SesMailer implements Mailer {
  constructor(
    private readonly client = new SESv2Client({}),
    private readonly from = "orders@shop.example",
  ) {}

  async send(mail: Mail): Promise<void> {
    await this.client.send(
      new SendEmailCommand({
        FromEmailAddress: this.from,
        Destination: { ToAddresses: [mail.to] },
        Content: {
          Template: { TemplateName: mail.template, TemplateData: JSON.stringify(mail.data) },
        },
      }),
    );
  }
}
