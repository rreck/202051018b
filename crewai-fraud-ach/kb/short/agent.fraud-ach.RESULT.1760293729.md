```json
{
  "id": "4da830af14817932",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293729,
  "host_pid": "9e6742732c60:1",
  "hash": "33172efc09b181b3dceaa70ae44ff31df22e9414496d7b1cdef0304bac939d80",
  "cid": "QmV133172efc09b181b3dceaa70ae44ff31df22e9414",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293729,
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
      "evaluated_at": 1760293729
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
  "sig": "c7d5194616d09b72a5f45002867a3baddc29392eef9c7fc5aaef773bbf8f0547"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596468860
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 16941120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'e06c0748f018586e'}}}