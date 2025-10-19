```json
{
  "id": "7546ce15a5fe63bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294135,
  "host_pid": "9e6742732c60:1",
  "hash": "760dc4d62803a0fba53a57463e0549fd47d92ae97c57e23f867c1fcb3b384b45",
  "cid": "QmV1760dc4d62803a0fba53a57463e0549fd47d92ae9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294135,
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
      "evaluated_at": 1760294135
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
  "sig": "876e0fd13b2b283423af4ecd1060f858f0fd3286786ad32708b86af15ff40662"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245693870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 59669704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '3f6bcdf181d34e46'}}}}