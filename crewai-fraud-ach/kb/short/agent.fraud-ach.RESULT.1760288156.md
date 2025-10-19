```json
{
  "id": "899f41368d4ed0fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288156,
  "host_pid": "9e6742732c60:1",
  "hash": "84d5276976c0bb999545ed77903f0f7cbb69c78293c9cc5c4ff985d5e38acd55",
  "cid": "QmV184d5276976c0bb999545ed77903f0f7cbb69c782",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288156,
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
      "evaluated_at": 1760288156
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
  "sig": "4a7896a570d75ac624f1a9e9bdf487a0ae640c2734ca1dff7972267c46c464b9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034020503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285765, 'matching_hash': '8db66b2beb557931'}}}