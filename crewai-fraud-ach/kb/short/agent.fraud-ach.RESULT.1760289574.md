```json
{
  "id": "d400ec7e17fd0784",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289574,
  "host_pid": "9e6742732c60:1",
  "hash": "dfe46006666b3379e35656760670e40cf1ae5f5bf8598b32f70fa40cf28c7406",
  "cid": "QmV1dfe46006666b3379e35656760670e40cf1ae5f5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289574,
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
      "evaluated_at": 1760289574
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
  "sig": "2b3d3c99d11cdc5582b14140108703df1e494dea396d5ca6b9c75af7995aa8bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036013549
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 51838225, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': 'f1471db42dbf1c81'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}