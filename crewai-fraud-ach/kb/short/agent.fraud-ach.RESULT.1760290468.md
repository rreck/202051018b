```json
{
  "id": "9fb0430d075672ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290468,
  "host_pid": "9e6742732c60:1",
  "hash": "33f4c85a3f0e046b5286ad4b6c33655b214942b911761dc89ad0d639bf8e6aea",
  "cid": "QmV133f4c85a3f0e046b5286ad4b6c33655b214942b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290468,
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
      "evaluated_at": 1760290468
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
  "sig": "50797255f6f1d9ae69f6370524ea427d9a837ff8477e45c17bf2ab963037581e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039536800
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 26980982, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': '37ca22243c3304cf'}}}