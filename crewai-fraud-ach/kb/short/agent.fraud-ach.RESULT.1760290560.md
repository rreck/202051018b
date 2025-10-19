```json
{
  "id": "d5e91c3df88a5f6c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290560,
  "host_pid": "9e6742732c60:1",
  "hash": "d45580b7abeb0a1ffc481d6006791caaca4d777198c79b30eb1765dd315a2785",
  "cid": "QmV1d45580b7abeb0a1ffc481d6006791caaca4d7771",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290560,
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
      "evaluated_at": 1760290560
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
  "sig": "b1f3f585f8c85a03ddbeeda27a33ba8b88ff2c55b18a0da897fcae5af5b6b165"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039834912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 53267868, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285765, 'matching_hash': '21095e194860d742'}}}