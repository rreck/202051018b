```json
{
  "id": "9964213def33e83e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290831,
  "host_pid": "9e6742732c60:1",
  "hash": "e987d14bc7207296e2ae811a57d75183ecd1317b434bbaa84af553274a3d421f",
  "cid": "QmV1e987d14bc7207296e2ae811a57d75183ecd1317b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290831,
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
      "evaluated_at": 1760290831
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
  "sig": "69d200bc6bf1cd557134aa12c9d9e75e49881e2dd08af737f6810a1e2f2e0594"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243277611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 22527040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}