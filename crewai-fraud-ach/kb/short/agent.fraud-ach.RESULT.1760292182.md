```json
{
  "id": "88bddc680bf6b08a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292182,
  "host_pid": "9e6742732c60:1",
  "hash": "c382ef949da6b907aac2161ef3e405e8e1685d2de50e9834bb8f5c478ba93c9c",
  "cid": "QmV1c382ef949da6b907aac2161ef3e405e8e1685d2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292182,
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
      "evaluated_at": 1760292182
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
  "sig": "d02bf9e73edd5c7476066066eb7387e7460be186721aada046048fe796606a5f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026087105
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 56304192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': '109bc77652f62494'}}}