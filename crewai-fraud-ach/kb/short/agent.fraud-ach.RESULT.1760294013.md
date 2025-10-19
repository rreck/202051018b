```json
{
  "id": "0305c131d2b68ccb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294013,
  "host_pid": "9e6742732c60:1",
  "hash": "4124b57bbf76743f77b2ce23c550f568d693b7ad8c4a37dac4f77fdbb35fb73c",
  "cid": "QmV14124b57bbf76743f77b2ce23c550f568d693b7ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294013,
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
      "evaluated_at": 1760294013
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
  "sig": "e73e0cef54281dcdc3c30ac2a592da67e541600ff2a59bd7591e93a4563891ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 30711210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}maly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.69, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7209366}}}