```json
{
  "id": "56302e6c40673c3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290134,
  "host_pid": "9e6742732c60:1",
  "hash": "fe0f7caa85175c948da5c16ab81a457a58176de80820dd85f61e7c8a9b7d04b4",
  "cid": "QmV1fe0f7caa85175c948da5c16ab81a457a58176de8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290134,
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
      "evaluated_at": 1760290134
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
  "sig": "fa65eaceaecbec98ef243f11645a1022168923b37650853c50f64c095539f82d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152430853
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 11968754, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285764, 'matching_hash': 'fa17beca2cfad33c'}}}