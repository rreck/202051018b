```json
{
  "id": "91ec8f9d02f786b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294915,
  "host_pid": "9e6742732c60:1",
  "hash": "faa2ebaf1b8532ed03990ed7723a2b9349c260cc9a873e83929706b520e53910",
  "cid": "QmV1faa2ebaf1b8532ed03990ed7723a2b9349c260cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294915,
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
      "evaluated_at": 1760294915
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
  "sig": "197ac8de8276003af4ed54bffdab81aed2be97ca3702fff9a0e7c74dc11384d7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156708491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 24004942, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '1bac7a606fc9693a'}}}