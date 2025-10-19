```json
{
  "id": "115bff3ae26b85f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293022,
  "host_pid": "9e6742732c60:1",
  "hash": "e2d830a12ecad8826f29ccfba84fdbcf96ce8373339964e76be9463e59df420a",
  "cid": "QmV1e2d830a12ecad8826f29ccfba84fdbcf96ce8373",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293022,
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
      "evaluated_at": 1760293023
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
  "sig": "548f331e4b35093002b82e3539ba0a91cb4232a0759ef868b1278f3e4648fd8b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021252160
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 99959580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '942f41a705b17558'}}}