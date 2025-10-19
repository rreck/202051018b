```json
{
  "id": "615bbb1e565d0fe6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288329,
  "host_pid": "9e6742732c60:1",
  "hash": "4c273aadd84c2ce0cc7391466648efb194f9e415d081e071e1e8f0ec404e172d",
  "cid": "QmV14c273aadd84c2ce0cc7391466648efb194f9e415",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288329,
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
      "evaluated_at": 1760288329
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
  "sig": "3ae67acb9d662fefd9358d9637ee55d2c39dad498668a10340496e9adacd9084"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591167362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 28086480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285763, 'matching_hash': '24df3db171a5add1'}}}