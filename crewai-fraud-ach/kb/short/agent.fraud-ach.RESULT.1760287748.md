```json
{
  "id": "1831d476658854e7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287748,
  "host_pid": "9e6742732c60:1",
  "hash": "e417b1279866c9a176d1b497ced861110ec938da1921c3b41af63641f3071dee",
  "cid": "QmV1e417b1279866c9a176d1b497ced861110ec938da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287748,
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
      "evaluated_at": 1760287748
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
  "sig": "617033c6eecc508843249aaca27521124c7d03544494fb2c3691fb7e3b859cb3"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 044000031117260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285763, 'matching_hash': '467ec1c9bc787c3f'}}}een': 1760285763, 'matching_hash': '276303153292771e'}}}