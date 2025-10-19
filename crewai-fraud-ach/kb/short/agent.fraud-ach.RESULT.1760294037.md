```json
{
  "id": "ec155efdc1c32b43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294037,
  "host_pid": "9e6742732c60:1",
  "hash": "f925c92fd0a13b9b81b0e10a3470104eac097a0da2b2e5c518c0ccd006b4743a",
  "cid": "QmV1f925c92fd0a13b9b81b0e10a3470104eac097a0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294037,
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
      "evaluated_at": 1760294037
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
  "sig": "371c6bae2c02dbf8513e780d872f7d9e88127b2b504f7e5b18018d19ef7ed867"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 68260550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}