```json
{
  "id": "544ba5441f5011ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292660,
  "host_pid": "9e6742732c60:1",
  "hash": "f1882684eec7c1f7ac45610c40788e13777d32ac0137ce781ce83ba4ed7916a2",
  "cid": "QmV1f1882684eec7c1f7ac45610c40788e13777d32ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292660,
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
      "evaluated_at": 1760292660
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
  "sig": "5e7602764e75624d525c36c4e7ddd62f0bb7b4968a5b471a2a5314584d6af6fb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 68893716, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}