```json
{
  "id": "34139ff0cf1712cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287881,
  "host_pid": "9e6742732c60:1",
  "hash": "453db4d0ac9b24c941034d0aec6874097af703ebe144e3c818e338266e21623a",
  "cid": "QmV1453db4d0ac9b24c941034d0aec6874097af703eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287881,
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
      "evaluated_at": 1760287881
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
  "sig": "79d9f4a6dfa791ade9c052448865ce7e69289b831398f67e7243e6ecd6b8a74d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022318038
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 18035400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285765, 'matching_hash': 'c47c52aff7a65053'}}}