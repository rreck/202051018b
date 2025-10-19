```json
{
  "id": "237af7e614b27bdc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287995,
  "host_pid": "9e6742732c60:1",
  "hash": "ba35a94636fbe145caefafb210ee82f213efda52b5a2a8a1da63a13824865c50",
  "cid": "QmV1ba35a94636fbe145caefafb210ee82f213efda52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287995,
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
      "evaluated_at": 1760287995
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
  "sig": "b514c64f32b4c7ab4e733292bef7495a7bf340f20ec88894d3671990f44f4b77"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020703113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 22715897, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285763, 'matching_hash': '6c2ac9b0cec56c2f'}}}