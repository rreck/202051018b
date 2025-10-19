```json
{
  "id": "4c99f8bb1241ed38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293515,
  "host_pid": "9e6742732c60:1",
  "hash": "c01ea8ec49745ff39f9c752e963ddd6b0f2e2da6db8caeb00adf080f65430332",
  "cid": "QmV1c01ea8ec49745ff39f9c752e963ddd6b0f2e2da6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293515,
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
      "evaluated_at": 1760293515
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
  "sig": "61a479d1e185c5f48ed579e50cc24dd8aa96731d9d57fec0670ce437f4d873ed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276282888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 84021960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '2c6b6a2c3736dbce'}}}