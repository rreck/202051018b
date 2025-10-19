```json
{
  "id": "6d4f07891e19eb68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290770,
  "host_pid": "9e6742732c60:1",
  "hash": "6ad0df46dc20e2a3cfa4b1a107c241e46727fb21d1fdffa93cb5b59ed525bb7d",
  "cid": "QmV16ad0df46dc20e2a3cfa4b1a107c241e46727fb21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290770,
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
      "evaluated_at": 1760290770
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
  "sig": "e806d77849cf691dd6cb5d31a2dfc16f77fab29da453f8733b1f9cae65db6f6c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467386779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 39750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': 'cfffbd2ec30a8ce4'}}}maly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.38, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6664302}}}