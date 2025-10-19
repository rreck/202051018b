```json
{
  "id": "9560f54548e5795b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289864,
  "host_pid": "9e6742732c60:1",
  "hash": "6ac542876a87dcf8e80c868196a849995e8641531ce60b197d60395e2248ce5d",
  "cid": "QmV16ac542876a87dcf8e80c868196a849995e864153",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289864,
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
      "evaluated_at": 1760289864
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
  "sig": "0c128129e2f736f32b4035e3ed3f5248da75b755bbe2677618211b683fc9eddf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154224764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 32600475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': '73218c90107a537b'}}}