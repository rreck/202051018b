```json
{
  "id": "f1c5d84d93792e74",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285846,
  "host_pid": "9e6742732c60:1",
  "hash": "6c3ec7966d859b0f0c2e3f9180259db41a12d52914ed1dee4a3d9a708e3409a2",
  "cid": "QmV16c3ec7966d859b0f0c2e3f9180259db41a12d529",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285846,
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
      "evaluated_at": 1760285846
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
  "sig": "add7926467986558fdd47b273d12548dd5db4a31a2e84508215d9412e7c5825b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246878582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 22093560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760284979, 'matching_hash': '3e968f91ba41b0b5'}}}