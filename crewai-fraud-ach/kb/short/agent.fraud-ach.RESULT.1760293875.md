```json
{
  "id": "4b6148ae3cec6418",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293875,
  "host_pid": "9e6742732c60:1",
  "hash": "15029e0f751ac73acdec38a591199d8128bb5a5bee8cd5900d9fa3d9786b8f73",
  "cid": "QmV115029e0f751ac73acdec38a591199d8128bb5a5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293875,
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
      "evaluated_at": 1760293875
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
  "sig": "4c3fea445bd6a33ff1eb3bb6c2d7864da001d706e900e18210c21174b200d993"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 303, 'threshold': 50, 'total_amount': 80009574, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 302, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}maly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.08, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6131353}}}