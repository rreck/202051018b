```json
{
  "id": "0f35231cf5620f94",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289096,
  "host_pid": "9e6742732c60:1",
  "hash": "36b4dc063986152042ccf9b4ae1c559deb710e97e84762f7ae253eab3fab2ab0",
  "cid": "QmV136b4dc063986152042ccf9b4ae1c559deb710e97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289096,
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
      "evaluated_at": 1760289096
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
  "sig": "4db0e037cbeac9a04aa6c73af2ddaf79e17db2a113ada88bbf2f346e299d0165"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279407211
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 24571285, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285764, 'matching_hash': 'efd9a787beb40cb2'}}}