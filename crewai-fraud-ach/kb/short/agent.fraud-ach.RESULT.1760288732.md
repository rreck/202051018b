```json
{
  "id": "892aa301f7fff7c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288732,
  "host_pid": "9e6742732c60:1",
  "hash": "6893c9e772bf88cbbdfd7ac4748439b1c93cde957891beb3002d93b2eed12301",
  "cid": "QmV16893c9e772bf88cbbdfd7ac4748439b1c93cde95",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288732,
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
      "evaluated_at": 1760288732
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
  "sig": "2c39b398bc7bf1ce56a8a825679f1f6575bc70301306e43cfa568377b570b0bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025832040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 45735066, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285764, 'matching_hash': '02af8ad93f509b45'}}}