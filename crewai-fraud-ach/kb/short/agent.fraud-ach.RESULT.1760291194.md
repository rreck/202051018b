```json
{
  "id": "afe747230e51a680",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291194,
  "host_pid": "9e6742732c60:1",
  "hash": "cbbeae08eb1a519e8f6fc426a7a3f8b48afb8c65486d6f1b33fb538cf839dcca",
  "cid": "QmV1cbbeae08eb1a519e8f6fc426a7a3f8b48afb8c65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291194,
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
      "evaluated_at": 1760291194
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
  "sig": "0f712e4ff3b32f9f0a1ca5a9d6da792bd4cd18386754a6ef1a7452558f0e8c79"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037692858
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 31928890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760284979, 'matching_hash': '7018b288608f6738'}}}