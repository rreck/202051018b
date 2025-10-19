```json
{
  "id": "8bcc82fe3e251943",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286667,
  "host_pid": "9e6742732c60:1",
  "hash": "2e2a8620558f811d81b0603f4ffceef097d189dedcf6802f51be9f63e749cdbb",
  "cid": "QmV12e2a8620558f811d81b0603f4ffceef097d189de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286667,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286667
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8a2985078376986b305795993be532a50f12c7f786b04ed9542dcc06c8db1f0d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201467071616
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14841552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285764, 'matching_hash': 'cbd6f8586f75cfb9'}}}