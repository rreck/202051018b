```json
{
  "id": "349ce49a2c24f84e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290363,
  "host_pid": "9e6742732c60:1",
  "hash": "b539d98b3be14b69959d09b50153f4bdaac349d7f9d6beee50ce624265a2041b",
  "cid": "QmV1b539d98b3be14b69959d09b50153f4bdaac349d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290363,
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
      "evaluated_at": 1760290363
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
  "sig": "fe17a8cb372fbe8bdd2311d1faeed73e83c85068afc2ea2ba2e4565a4a81d9c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240153207
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 37000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285764, 'matching_hash': '9e24c0ed91a48db3'}}}