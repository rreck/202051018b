```json
{
  "id": "1b81b4e9f1b679af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287045,
  "host_pid": "9e6742732c60:1",
  "hash": "03be0f435d8d89b2141ba4d58aa6a213597f4ec11026143a5867ecdc7ae91bd8",
  "cid": "QmV103be0f435d8d89b2141ba4d58aa6a213597f4ec1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287045,
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
      "evaluated_at": 1760287045
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
  "sig": "f1773a2f3090674a138bfc0b7079282e9bb4b7e34d23c2f0932cd647b42d36f6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105155616727
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': 'b26c49bc45dba458'}}}