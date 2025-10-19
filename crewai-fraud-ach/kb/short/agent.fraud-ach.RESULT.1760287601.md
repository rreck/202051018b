```json
{
  "id": "f80337a87a867a3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287601,
  "host_pid": "9e6742732c60:1",
  "hash": "2261707abd7945e12f83eb3d2b85e5e5d99a2110143a49cd78018acf91397aec",
  "cid": "QmV12261707abd7945e12f83eb3d2b85e5e5d99a2110",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287601,
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
      "evaluated_at": 1760287601
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
  "sig": "7b836b73e6bb59b8ce9adf5854a83a0eea99c2dd5e3339298b73bc6be10486fe"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 111000025654087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285763, 'matching_hash': '431eabbdd05dc2b1'}}}een': 1760285763, 'matching_hash': 'c24831f619c6556e'}}}