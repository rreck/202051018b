```json
{
  "id": "660a175a8c53e855",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290236,
  "host_pid": "9e6742732c60:1",
  "hash": "d6cce016fc2c058eda2db98e624a5a26f9945459e6144fb04673264bb1acf9e2",
  "cid": "QmV1d6cce016fc2c058eda2db98e624a5a26f9945459",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290236,
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
      "evaluated_at": 1760290236
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
  "sig": "f2790657ad39369c93220724b54220ed7541692046c66b7cb3c93b517ad2b806"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035326391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 54186210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': '7c05ec5f373172f0'}}}