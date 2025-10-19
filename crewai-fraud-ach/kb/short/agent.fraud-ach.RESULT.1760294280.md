```json
{
  "id": "0763736b243e990a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294280,
  "host_pid": "9e6742732c60:1",
  "hash": "be64dc3691590ac53eae537dbe3ec293a1f82af4532ec235e452ba94b6b648ce",
  "cid": "QmV1be64dc3691590ac53eae537dbe3ec293a1f82af4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294280,
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
      "evaluated_at": 1760294280
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
  "sig": "589df5d5761b0fdff835b40d60ed8d1cfb6b63ff0dc64ba62ac508b48582d274"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468298709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 14802415, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '7ee51499d35b3ada'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8018325}}}