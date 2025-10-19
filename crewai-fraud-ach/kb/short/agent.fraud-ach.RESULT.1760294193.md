```json
{
  "id": "66555ecaf5d18eec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294193,
  "host_pid": "9e6742732c60:1",
  "hash": "b70900c3ab3f249059377b6f27965d8b78da629a90abce62533a64ea91318e48",
  "cid": "QmV1b70900c3ab3f249059377b6f27965d8b78da629a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294193,
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
      "evaluated_at": 1760294193
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
  "sig": "701498459136a6991144f0624d8ca3ec6d79a6ca5d8d9fca3062ad45bf5bafe5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245381675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 38216893, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': 'fa6674ee96d393a2'}}}