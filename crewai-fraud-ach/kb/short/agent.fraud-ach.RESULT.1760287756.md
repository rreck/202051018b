```json
{
  "id": "6815d1bc18df4c8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287756,
  "host_pid": "9e6742732c60:1",
  "hash": "153def639b36f0540bcd5d3ae493e04ec47405a6bf1733b2734ff1557eda9c1c",
  "cid": "QmV1153def639b36f0540bcd5d3ae493e04ec47405a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287756,
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
      "evaluated_at": 1760287756
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
  "sig": "9686b4d616c21e01bfa2dd0cef6761608b3ea1b08b440f18c88ae5ae58f6fc43"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 121000243277611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}