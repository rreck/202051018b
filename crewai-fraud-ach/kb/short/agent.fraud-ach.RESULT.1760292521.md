```json
{
  "id": "71e08be8fe61481e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292521,
  "host_pid": "9e6742732c60:1",
  "hash": "c485cb88a36754e98548c9b89b34288ffb6dee7a52860d6446cc398cf6cedd3d",
  "cid": "QmV1c485cb88a36754e98548c9b89b34288ffb6dee7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292521,
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
      "evaluated_at": 1760292521
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
  "sig": "342c0cf092c4415d082c79c7433afd484ab37b45b611750c028f64897428d004"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240953214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 11798511, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285764, 'matching_hash': 'cfdb33c4cfd6ba9b'}}}