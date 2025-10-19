```json
{
  "id": "7e5a8411a72e6498",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290621,
  "host_pid": "9e6742732c60:1",
  "hash": "8967a541dc705abc84a8dfa21cccb5b2b192330243c0ec0922cfaaf9a94f7039",
  "cid": "QmV18967a541dc705abc84a8dfa21cccb5b2b1923302",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290621,
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
      "evaluated_at": 1760290621
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
  "sig": "022a261ef821a598a6771fc5d08f769b027caf44fd8dde833915c274a24af7bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150592686
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '43d52159a9989a8b'}}}een': 1760285764, 'matching_hash': '20b3840d87952e5c'}}}