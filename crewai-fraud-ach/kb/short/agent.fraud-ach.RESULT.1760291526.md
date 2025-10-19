```json
{
  "id": "aaf8c633055c0842",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291526,
  "host_pid": "9e6742732c60:1",
  "hash": "4374e0b029505c637ab2655e99c1c80c0f1c1d3f71aa85105a8a93e6e361cd54",
  "cid": "QmV14374e0b029505c637ab2655e99c1c80c0f1c1d3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291526,
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
      "evaluated_at": 1760291526
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
  "sig": "db96b76f273081d74fc5b5bd0d68d954ed72bdcccfd1666114504fe6d085efd0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029744317
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 48681372, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285764, 'matching_hash': '20edeb4e835a4770'}}}