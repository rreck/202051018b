```json
{
  "id": "0ea3b22b63c17723",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290385,
  "host_pid": "9e6742732c60:1",
  "hash": "14bc743e7a8816e6846f4859f7078c7dc23169e3bf8976592c6793597386f028",
  "cid": "QmV114bc743e7a8816e6846f4859f7078c7dc23169e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290385,
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
      "evaluated_at": 1760290385
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
  "sig": "6780db2c8e5da1642f3f0fa30c90d3810ecdb0ecce578b4b6c73b5e5c09ce5e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025820321
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 38414882, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': 'cf65bb25527720c5'}}}