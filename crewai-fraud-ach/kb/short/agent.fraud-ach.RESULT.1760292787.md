```json
{
  "id": "bee7c0d129bef431",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292787,
  "host_pid": "9e6742732c60:1",
  "hash": "61ef867f534ce0d13c8177579ca2c9693f7ecba782f80ee8e2f3553bfa725101",
  "cid": "QmV161ef867f534ce0d13c8177579ca2c9693f7ecba7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292787,
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
      "evaluated_at": 1760292787
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
  "sig": "f367e5a986a3e7cd02a935a39bc760b86d5183f807d870929fe72d3ff730c5e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469045536
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 70284045, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': 'd92613c41315e1ec'}}}