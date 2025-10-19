```json
{
  "id": "68b3615860664f47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292108,
  "host_pid": "9e6742732c60:1",
  "hash": "881f157f740c956ef43de9d69630c68c4ae10b3882dc2b3daa98e98df852cc19",
  "cid": "QmV1881f157f740c956ef43de9d69630c68c4ae10b38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292108,
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
      "evaluated_at": 1760292108
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
  "sig": "735abe8e7d035e9ab9d864efca552901d942627ada67ab819b53c56d591fc392"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153385568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': '556aff2bced704f0'}}}