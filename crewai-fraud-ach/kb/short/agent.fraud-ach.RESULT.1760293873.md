```json
{
  "id": "7d184201427b9b34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293873,
  "host_pid": "9e6742732c60:1",
  "hash": "d82c66dd4d72003b04cab4c4de6f22c941798d35737558ccea22d92eca0ac18b",
  "cid": "QmV1d82c66dd4d72003b04cab4c4de6f22c941798d35",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293873,
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
      "evaluated_at": 1760293873
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
  "sig": "807b545b2fbe9541cd086138fff7e33f6c28495d25aafb243901f8c02d7b5c9e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027976584
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 70048341, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '76d4e63915320a3d'}}}