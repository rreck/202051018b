```json
{
  "id": "533ab53947efdcf8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291278,
  "host_pid": "9e6742732c60:1",
  "hash": "aa924d4a054fb5b95ea6ab54b2c4cbdc1d862b3cbcafa41e0dfc07333d93de6f",
  "cid": "QmV1aa924d4a054fb5b95ea6ab54b2c4cbdc1d862b3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291278,
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
      "evaluated_at": 1760291278
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "11e00128203c1eb3a7848339ff16a209315bff87af27c79ddf7d9d538c0c2a5c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594081907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 84739734, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': 'b8f6a044d6b1da81'}}}