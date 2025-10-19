```json
{
  "id": "9a845ed3bb61e9ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294130,
  "host_pid": "9e6742732c60:1",
  "hash": "7897915a5faad032ebfd68924468a80d58dc691bf4c2548a01fc9cf40141a349",
  "cid": "QmV17897915a5faad032ebfd68924468a80d58dc691b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294130,
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
      "evaluated_at": 1760294130
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
  "sig": "2bec9a743d3699ca6bf296a0d63cb2ca674a40cc87a5cbd1ebbd0a8a9136d9c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152772165
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 67420592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285764, 'matching_hash': '9371db7725d4e0a9'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}