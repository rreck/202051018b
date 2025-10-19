```json
{
  "id": "f84c9fc96a25141f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292005,
  "host_pid": "9e6742732c60:1",
  "hash": "a60490b61a4f415df9a814b49e9493281415e0378cf04ea1dd32d608e1f1992e",
  "cid": "QmV1a60490b61a4f415df9a814b49e9493281415e037",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292005,
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
      "evaluated_at": 1760292005
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
  "sig": "8f778839a36d6e4e298b084a6c21466994910a380804353355c52162435cd65c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153448153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 90848556, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285764, 'matching_hash': '55db9843fa0daece'}}}