```json
{
  "id": "d583bb6ea9844826",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288031,
  "host_pid": "9e6742732c60:1",
  "hash": "62287bc2ed96fa0143c5abc018d6e8c675dcac113627d754779c86c85d2f9e54",
  "cid": "QmV162287bc2ed96fa0143c5abc018d6e8c675dcac11",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288031,
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
      "evaluated_at": 1760288031
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
  "sig": "b65e0d70a90ddba9d4a7cd44066988cf8173239cf77c7c775cae8d92ec72ac3a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038917834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 23239360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285765, 'matching_hash': '760f57350f86dbe3'}}}