```json
{
  "id": "5af76c960d8f1154",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287046,
  "host_pid": "9e6742732c60:1",
  "hash": "7e8c11eab687d6557ad04edacac32051a09cc37a9ed7b6dd0cd617b7ee1dab71",
  "cid": "QmV17e8c11eab687d6557ad04edacac32051a09cc37a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287046,
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
      "evaluated_at": 1760287046
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
  "sig": "ce3635c5268835d09c868dec3a7c57128267b6add0369529741089293162f6b8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000020141329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21732700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285764, 'matching_hash': '1e11ace6091d7a38'}}}