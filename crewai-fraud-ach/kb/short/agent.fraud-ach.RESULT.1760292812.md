```json
{
  "id": "2f2c8a938b192843",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292812,
  "host_pid": "9e6742732c60:1",
  "hash": "730696237f9910b22c868f2f7d6c88b847a7445239a8775784b4460025e9bb5a",
  "cid": "QmV1730696237f9910b22c868f2f7d6c88b847a74452",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292812,
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
      "evaluated_at": 1760292812
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
  "sig": "b994d5111525cdb789905d3964f80e5f4fa9cdb98e13ce2d890b00e1fec4b4eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 65240840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}