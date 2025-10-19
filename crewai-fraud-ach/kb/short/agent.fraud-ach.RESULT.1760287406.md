```json
{
  "id": "f2b6aa2413164b54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287406,
  "host_pid": "9e6742732c60:1",
  "hash": "4647566631cdcf3b7838073603a78262efc4581f189e2d041e195fb1600ef234",
  "cid": "QmV14647566631cdcf3b7838073603a78262efc4581f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287406,
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
      "evaluated_at": 1760287406
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
  "sig": "55b00ca154afaee544760c08b8100acb3e599ca25af5c5d249d5cb9fcd70f68f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201461386979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 20039409, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285764, 'matching_hash': '1569de4be841c048'}}}