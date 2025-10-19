```json
{
  "id": "09f2225c4283b311",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294732,
  "host_pid": "9e6742732c60:1",
  "hash": "1b70627b88c563c52976ee946197dfdd74ccf129ff4167778f224a76d5dff5d9",
  "cid": "QmV11b70627b88c563c52976ee946197dfdd74ccf129",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294732,
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
      "evaluated_at": 1760294732
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
  "sig": "46b8a4c4b898cf90aa272ad0d37d166c016ab901c789a0d1501b585eb6b991c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247499118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 18589014, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': 'f65a723d753f6ade'}}}