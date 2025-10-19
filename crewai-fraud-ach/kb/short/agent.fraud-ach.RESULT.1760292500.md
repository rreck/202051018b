```json
{
  "id": "20784cc70dc93733",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292500,
  "host_pid": "9e6742732c60:1",
  "hash": "aa9d1d51676b9b85ff88eac731e1f2504c93c825ca2838bad414589f31e6f76f",
  "cid": "QmV1aa9d1d51676b9b85ff88eac731e1f2504c93c825",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292500,
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
      "evaluated_at": 1760292500
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
  "sig": "434656d5e435a7512a1546038ef73b19c56ed1b5ad98292074cdf4988f998b43"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037838000
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 23260911, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': 'ae4ad01d54e54763'}}}