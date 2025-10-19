```json
{
  "id": "4af7dcf98d7a161e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292587,
  "host_pid": "9e6742732c60:1",
  "hash": "a2d2bdec4a9c5e87f2562fc9add877f2b0a6e55b9fdbc029be9e44d21a5bf8a4",
  "cid": "QmV1a2d2bdec4a9c5e87f2562fc9add877f2b0a6e55b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292587,
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
      "evaluated_at": 1760292587
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
  "sig": "f5e66244f5f65b539e22371eb490518af16977abb9ecb979332e15a614a52119"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596228343
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 20100000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '964edcfaddb10414'}}}