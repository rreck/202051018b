```json
{
  "id": "a8ef19280f6d2039",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286963,
  "host_pid": "9e6742732c60:1",
  "hash": "c4c5966de502cbdc712c6d78fe94cbe87bcb6963db7508a6317948d797c1009a",
  "cid": "QmV1c4c5966de502cbdc712c6d78fe94cbe87bcb6963",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286963,
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
      "evaluated_at": 1760286963
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
  "sig": "e7d00ef845add3fdc5c8d191a35bc66da58cb1577a63bbf4293949d9eaa02636"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009597956116
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15792610, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285764, 'matching_hash': '37dac3adff3764b9'}}}