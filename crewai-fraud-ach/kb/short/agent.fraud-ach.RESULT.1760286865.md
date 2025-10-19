```json
{
  "id": "8733133929e51d34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286865,
  "host_pid": "9e6742732c60:1",
  "hash": "25a8789b2c9d4cf9124caec2bf99dea665e796e3e92be0381b0c37a8713f1715",
  "cid": "QmV125a8789b2c9d4cf9124caec2bf99dea665e796e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286865,
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
      "evaluated_at": 1760286865
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
  "sig": "0df9a3486a026344ad14b02f7c543faf901ce3c1e0383945fc1e2e1ec2e7d296"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000027419247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18792840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285763, 'matching_hash': 'f49fdb64c00c5aec'}}}