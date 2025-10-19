```json
{
  "id": "2dd166d0830925a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292887,
  "host_pid": "9e6742732c60:1",
  "hash": "a212adfb86c9c3a2927590930669f49b56a8c4d063f64824a469eeed33d81113",
  "cid": "QmV1a212adfb86c9c3a2927590930669f49b56a8c4d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292887,
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
      "evaluated_at": 1760292887
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
  "sig": "4e221db96ae1ddd83d1dc73377ef53887d621d5045263187214219569557a2a5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024591055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 95921109, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '8a72f4eb6bbba5d7'}}}