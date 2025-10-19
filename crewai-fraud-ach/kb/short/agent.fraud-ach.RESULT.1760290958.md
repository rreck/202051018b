```json
{
  "id": "3d70f66a977a81b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290958,
  "host_pid": "9e6742732c60:1",
  "hash": "fa5aab932ac1e59ce774ea1abe8f5bab99e013210b6037b69982e66e3f9f56d2",
  "cid": "QmV1fa5aab932ac1e59ce774ea1abe8f5bab99e01321",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290958,
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
      "evaluated_at": 1760290958
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
  "sig": "ee8660f755ab9c496e0f7409b614aa84a845e62e7f9313e62f8d4b127364f903"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156610976
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 41593851, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285765, 'matching_hash': 'a1f55d60bf5ccf18'}}}