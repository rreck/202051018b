```json
{
  "id": "974dc9006052aa9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294900,
  "host_pid": "9e6742732c60:1",
  "hash": "ac003875bc669920f474548ecd2ae2354071ab285db69f74df35923e5db64f42",
  "cid": "QmV1ac003875bc669920f474548ecd2ae2354071ab28",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294900,
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
      "evaluated_at": 1760294900
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
  "sig": "5c79f1cc31bd30a55e43e90ce6405ee722adf2ccef7845f5cbf92542e0aba4d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153543170
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 23560650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': 'bc1f881c41cfe07c'}}}