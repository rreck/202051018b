```json
{
  "id": "8fea98ca041f0047",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294817,
  "host_pid": "9e6742732c60:1",
  "hash": "ade2c70986cae5ca8422c230a206c94b1db058cd3c967b0c76a0bad67ac4a08b",
  "cid": "QmV1ade2c70986cae5ca8422c230a206c94b1db058cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294817,
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
      "evaluated_at": 1760294817
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
  "sig": "30299e4e1fafa8e117b0cdc96ea3882aea4e8c1d11a71f427ad2daf126d6e0a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598799064
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 92186640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '14e8b5e643b0ea13'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8018325}}}