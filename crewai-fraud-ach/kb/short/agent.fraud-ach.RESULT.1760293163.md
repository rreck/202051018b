```json
{
  "id": "36cee5f0ec35d2c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293163,
  "host_pid": "9e6742732c60:1",
  "hash": "1db0fa341d957f61c8f9ea5f31e66d2c10a315d1044d2ce91976d6196c511801",
  "cid": "QmV11db0fa341d957f61c8f9ea5f31e66d2c10a315d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293163,
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
      "evaluated_at": 1760293163
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
  "sig": "5db68854634eac51ad16bb0287df1ae56f0f5ab363d330fc1bcbac4036e5060c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152274101
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 38212839, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': 'b0ffab0948116893'}}}