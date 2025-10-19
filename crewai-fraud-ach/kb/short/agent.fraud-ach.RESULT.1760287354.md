```json
{
  "id": "b3849db29e2eb31d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287354,
  "host_pid": "9e6742732c60:1",
  "hash": "f8c6fe8ce70166d22a4facc98ab8cdca9bc6326fae43c9749bdd9ed6001d603f",
  "cid": "QmV1f8c6fe8ce70166d22a4facc98ab8cdca9bc6326f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287354,
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
      "evaluated_at": 1760287354
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
  "sig": "a8044efc89ee7710f61d47bf10c4cc3df7d1714c1b9d4f60a07b41fc4f061b05"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026783731
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 23451852, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285763, 'matching_hash': 'dea6d8bb62de6c67'}}}