```json
{
  "id": "4e0251fa360ca4a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291370,
  "host_pid": "9e6742732c60:1",
  "hash": "8192191b9a440ec1bce8c3bc3061891c6730c33563045ec17a58566c67a35e5c",
  "cid": "QmV18192191b9a440ec1bce8c3bc3061891c6730c335",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291370,
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
      "evaluated_at": 1760291370
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
  "sig": "257f70ee1b00701b0ba9f97cdc1fb85828dccce38bdcbee824ba52b59fa9f0dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460644681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 59038499, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285764, 'matching_hash': '02c671505c0a8698'}}}