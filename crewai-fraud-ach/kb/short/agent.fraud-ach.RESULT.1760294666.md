```json
{
  "id": "7d220686fcb75fcb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294666,
  "host_pid": "9e6742732c60:1",
  "hash": "5c058abb9f67f8dd35218c2b5690cce693ff2315b6e93a51f15e5c11c72e7c05",
  "cid": "QmV15c058abb9f67f8dd35218c2b5690cce693ff2315",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294666,
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
      "evaluated_at": 1760294666
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "5666d1a1e855ab8d7656958e3f63c9da3c05d7322f9eae66f1ff9478a87fbe4e"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000029388663
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 318, 'threshold': 50, 'total_amount': 3114972180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 317, 'first_seen': 1760284979, 'matching_hash': '503d742180c16441'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9795510}}}