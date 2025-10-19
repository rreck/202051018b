```json
{
  "id": "421c9396e9d7cd8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294045,
  "host_pid": "9e6742732c60:1",
  "hash": "80d6393675566552b5c525e9606e663ba3cf370c00605b2bc0d369e33df01826",
  "cid": "QmV180d6393675566552b5c525e9606e663ba3cf370c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294045,
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
      "evaluated_at": 1760294045
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
  "sig": "ae1129dfd7827a306c2fb206f2127754ed1ea15184d27dc7a09190ce93ed2f9c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021517830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 68467090, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285765, 'matching_hash': '323b6ce2946b0561'}}}