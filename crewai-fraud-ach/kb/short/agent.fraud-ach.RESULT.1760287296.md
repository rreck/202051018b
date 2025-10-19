```json
{
  "id": "7e8a02475c2901cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287296,
  "host_pid": "9e6742732c60:1",
  "hash": "bf1b531ca2865de34a9dd3fcfdaf312d5cfef2deb99bd1ab531d5c2817d0d69c",
  "cid": "QmV1bf1b531ca2865de34a9dd3fcfdaf312d5cfef2de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287296,
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
      "evaluated_at": 1760287296
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "96f1b786e35cd5505750047733e840c7a16aa63da944c0bc224485a6079c728a"
}
```

Fraud detected: duplicate_transaction (score: 72)
Transaction: 044000039343574
Details: {'velocity': {'fraud_detected': True, 'risk_score': 60, 'details': {'transaction_count': 55, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285765, 'matching_hash': '13f5b4dcf27391fd'}}}een': 1760285763, 'matching_hash': 'cd477724f7ce5ce7'}}}