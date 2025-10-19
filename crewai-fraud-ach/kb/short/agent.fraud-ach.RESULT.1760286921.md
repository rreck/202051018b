```json
{
  "id": "e539db3fc6744ec4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286921,
  "host_pid": "9e6742732c60:1",
  "hash": "38f368d3eaf0af9788b1e071caa34c6667803bcc7359e2571cb910d8962a6887",
  "cid": "QmV138f368d3eaf0af9788b1e071caa34c6667803bcc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286921,
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
      "evaluated_at": 1760286921
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "36edbae792e5ce0ac701c8227249db100b9fbe73bbb507f3b6a653347d769e86"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000242269046
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16902900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285763, 'matching_hash': '94969c5585cd0fc1'}}}