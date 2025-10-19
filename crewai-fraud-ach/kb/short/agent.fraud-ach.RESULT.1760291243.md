```json
{
  "id": "13a924ec7511b482",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291243,
  "host_pid": "9e6742732c60:1",
  "hash": "c533dea469de42c1a1963724ffab31784d1f617c799229b2225c605eaf72d6b3",
  "cid": "QmV1c533dea469de42c1a1963724ffab31784d1f617c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291243,
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
      "evaluated_at": 1760291243
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
  "sig": "6873625241683b2382d57b6a813f5c76516c87c285a00b7940c189f7e6106b50"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277311413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': '8eaabbab3b444a6b'}}}