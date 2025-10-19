```json
{
  "id": "c03ce3328f22697a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290136,
  "host_pid": "9e6742732c60:1",
  "hash": "fe0a23777b94750b7124a47cc3aabb00a5403b18caafc9450e957f0a05e057ea",
  "cid": "QmV1fe0a23777b94750b7124a47cc3aabb00a5403b18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290136,
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
      "evaluated_at": 1760290136
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
  "sig": "e4ed284fe34956de3dcdf87445d125e0b625d8085a89a14e5eaca84d7e162eb7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037820415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285765, 'matching_hash': 'e2c6bf9b42825543'}}}