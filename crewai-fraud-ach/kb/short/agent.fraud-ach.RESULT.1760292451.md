```json
{
  "id": "418fbb2244070f8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292451,
  "host_pid": "9e6742732c60:1",
  "hash": "ba5ffe66f0aa424c455f2390654db3db13d79c2a701cea063ca7fc257b2e6f56",
  "cid": "QmV1ba5ffe66f0aa424c455f2390654db3db13d79c2a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292451,
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
      "evaluated_at": 1760292451
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
  "sig": "fe9b4d25eebff8b2b91d6685d7fa631b47ffac0e927da662c497e9c066c40d0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466146132
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 78572538, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': '20fb82cc575104fa'}}}