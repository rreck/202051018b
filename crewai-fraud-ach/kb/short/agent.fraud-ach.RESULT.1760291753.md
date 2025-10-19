```json
{
  "id": "1cf925783888f39c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291753,
  "host_pid": "9e6742732c60:1",
  "hash": "854b94e8820c99d8c45ed2af228aa3812a9ef07e1e45189f8969f92d93b24fdd",
  "cid": "QmV1854b94e8820c99d8c45ed2af228aa3812a9ef07e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291753,
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
      "evaluated_at": 1760291753
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
  "sig": "d59323b49b4e05a65cd8e15910d2c72b9d40e006253b494db1e7675b50724db9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598500621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 64904112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '36e427bddf577026'}}}