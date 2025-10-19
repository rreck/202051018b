```json
{
  "id": "2ba80a3ddb115111",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290356,
  "host_pid": "9e6742732c60:1",
  "hash": "a551281444c993531de136a86e97b9825eb23669a6e63b2b8fe9125551ecb7d0",
  "cid": "QmV1a551281444c993531de136a86e97b9825eb23669",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290356,
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
      "evaluated_at": 1760290356
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
  "sig": "a05ccb998a83fca18ca4d55102b6132ae79af752b58d9bba31e3608f3baf4fdd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461869062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 73524180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '24ed6b728fb62d75'}}}aly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.16, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6276049}}}