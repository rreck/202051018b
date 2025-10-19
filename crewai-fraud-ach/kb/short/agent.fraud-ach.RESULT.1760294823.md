```json
{
  "id": "92b7927ebab5a406",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294823,
  "host_pid": "9e6742732c60:1",
  "hash": "d3a01f74115a3a7fcacea366cdca579fb5af89832783ede325f33f24c52f5605",
  "cid": "QmV1d3a01f74115a3a7fcacea366cdca579fb5af8983",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294823,
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
      "evaluated_at": 1760294823
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
  "sig": "c1b7646712d0bb0470ec1bd619f623c12b72a41b50f502b179ebcede1fe208e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026959997
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 55646605, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': '4bd6adbc5f3cfca3'}}}