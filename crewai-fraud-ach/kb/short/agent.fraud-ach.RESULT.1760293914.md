```json
{
  "id": "89b9d9eba8bb1456",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293914,
  "host_pid": "9e6742732c60:1",
  "hash": "8f01190a854a3144790a162d4fb3c1e0bffbc3e27e3f86dd2fbb059768120571",
  "cid": "QmV18f01190a854a3144790a162d4fb3c1e0bffbc3e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293914,
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
      "evaluated_at": 1760293914
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
  "sig": "45156897544d7e61fbc6bc382969029cde167739ec9faea735708fa4721ef2ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025657387
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 72502176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': '1be88e7372567f08'}}}maly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9245331}}}