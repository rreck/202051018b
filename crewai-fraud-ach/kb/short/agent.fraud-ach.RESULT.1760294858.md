```json
{
  "id": "03b4cb8d1a37e0ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294858,
  "host_pid": "9e6742732c60:1",
  "hash": "fdeb2e09da4e2d9a0064104d050f6661b0b6dda518f5f1f7241ae59b08a93283",
  "cid": "QmV1fdeb2e09da4e2d9a0064104d050f6661b0b6dda5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294858,
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
      "evaluated_at": 1760294858
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
  "sig": "0a9f3a7bbf95c8f2083ace316f66099d367b68eb55d9cb70f1539aca0d790eaa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026803563
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 61712052, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': 'cf30c88fa01e3081'}}}