```json
{
  "id": "4459765accd44859",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291463,
  "host_pid": "9e6742732c60:1",
  "hash": "6e97642eeca8ed3c0a344d2627397386752d8ebdee29ce592859b63ae6f3b710",
  "cid": "QmV16e97642eeca8ed3c0a344d2627397386752d8ebd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291463,
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
      "evaluated_at": 1760291463
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
  "sig": "56de01f9cac70c0d5c7caffe72a0dceff6b9658e28e7fd9f7053781418f0527a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 55693400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}