```json
{
  "id": "164ce2d9e3fc4293",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293859,
  "host_pid": "9e6742732c60:1",
  "hash": "b0ad318d53cc396ab1dc57cf6d7977ac0ca347ef1c53b6a30a153c1e0c7777fe",
  "cid": "QmV1b0ad318d53cc396ab1dc57cf6d7977ac0ca347ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293859,
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
      "evaluated_at": 1760293859
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
  "sig": "e1ebd97e8605a5854f75478d7c5f5ad9febe9876b214cbae0900de2d725d72aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038197650
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 42691209, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '1b9150809eb731a5'}}}