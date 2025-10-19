```json
{
  "id": "30c9968684b2ce50",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292693,
  "host_pid": "9e6742732c60:1",
  "hash": "6a7fa6e31c237591aa9ecc8ef148c3ee9ec3f6353ba3709fa448f9880b771377",
  "cid": "QmV16a7fa6e31c237591aa9ecc8ef148c3ee9ec3f635",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292693,
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
      "evaluated_at": 1760292693
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
  "sig": "e3c103a0a4d7f78b95a86080a56107eacc5cebd3d9fe4ea29ab7e1d272ca696c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030474832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 77665567, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': 'bdea4d686a9b26f8'}}}