```json
{
  "id": "95c4cf5b39bb98fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287021,
  "host_pid": "9e6742732c60:1",
  "hash": "a8f350957f5360c518c13c118bc2168ea9f705aabd4e3d81a0500d11fd7875a4",
  "cid": "QmV1a8f350957f5360c518c13c118bc2168ea9f705aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287021,
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
      "evaluated_at": 1760287021
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
  "sig": "e8dbeea111ef917c94f960e96f9cc92d26574189fa77ec16084968b5c12b53c6"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201465632833
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21684780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285765, 'matching_hash': '908d3acbf69a371c'}}}