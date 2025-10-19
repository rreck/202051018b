```json
{
  "id": "425608097ca680b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291711,
  "host_pid": "9e6742732c60:1",
  "hash": "f192b53f3f866b65d400d4bd7253aa27260a403d84e111dcfe7324e3245a38d9",
  "cid": "QmV1f192b53f3f866b65d400d4bd7253aa27260a403d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291711,
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
      "evaluated_at": 1760291711
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
  "sig": "489b91634c781210059497356ea11d2f35da80576dad64093ce19a93f1a77de1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467134805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 49240145, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}