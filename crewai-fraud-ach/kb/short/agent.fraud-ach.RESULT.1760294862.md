```json
{
  "id": "5a46ca7bc11e327c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294862,
  "host_pid": "9e6742732c60:1",
  "hash": "dc2e95c3b66dfee771961bacb78c9b4c40cdcd415d5117ce3fefc284ee768d60",
  "cid": "QmV1dc2e95c3b66dfee771961bacb78c9b4c40cdcd41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294862,
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
      "evaluated_at": 1760294862
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
  "sig": "081b17c810fa3cd0850418c99676518fb31a9fd2a58ade458cb690abaa25be22"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025759024
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 94151826, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': 'fa026da4c6071776'}}}