```json
{
  "id": "e982ecc043742af0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292100,
  "host_pid": "9e6742732c60:1",
  "hash": "f623400a8d62d69808c53f6148030bf96faa4649524b28de2803290e85700b84",
  "cid": "QmV1f623400a8d62d69808c53f6148030bf96faa4649",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292100,
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
      "evaluated_at": 1760292100
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
  "sig": "cbc22ff31ae6db14b754b13c8666e0d33a5dbf8295c5ff21c56d137ce7443f7c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 68541360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}