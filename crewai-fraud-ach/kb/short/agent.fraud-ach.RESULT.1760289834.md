```json
{
  "id": "d5f748cdb3696d93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289834,
  "host_pid": "9e6742732c60:1",
  "hash": "90fb0af32e0be82f4a26471c27cd60bf9d0509fd1cf00f130461bd431177ca3b",
  "cid": "QmV190fb0af32e0be82f4a26471c27cd60bf9d0509fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289834,
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
      "evaluated_at": 1760289834
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
  "sig": "451078e98600b729753d425caca22c5cb23bb16b728b3850889741519e44ccb4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029265266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 49190462, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285764, 'matching_hash': 'a9619dd56a360910'}}}