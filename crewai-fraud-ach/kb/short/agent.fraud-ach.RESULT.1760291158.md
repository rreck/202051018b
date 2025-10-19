```json
{
  "id": "da20fc05f96880a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291158,
  "host_pid": "9e6742732c60:1",
  "hash": "aee3b12add56477a386629d661ea8dbb022e6b19ae2bc34653588be2014eca07",
  "cid": "QmV1aee3b12add56477a386629d661ea8dbb022e6b19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291158,
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
      "evaluated_at": 1760291158
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
  "sig": "d7eb6d5e4e9c25936938ae0ddb2f87894ed8dfbeaa8f83c807c293d56b46bbd3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 72395736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}