```json
{
  "id": "9290d601c26e62bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291653,
  "host_pid": "9e6742732c60:1",
  "hash": "bd02bf13d5ed4ae5237559be9679ce4d9052c22104f8b22accf8b52e2382b8eb",
  "cid": "QmV1bd02bf13d5ed4ae5237559be9679ce4d9052c221",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291653,
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
      "evaluated_at": 1760291653
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
  "sig": "f5f338d61ae685ce5198de1b39568dce7401573f8748510a604984bea0c0187b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154361187
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 45000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285764, 'matching_hash': 'a57b8c5e7960514a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}