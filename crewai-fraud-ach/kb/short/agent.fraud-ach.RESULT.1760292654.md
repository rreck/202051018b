```json
{
  "id": "461769d298cace4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292654,
  "host_pid": "9e6742732c60:1",
  "hash": "e06e6381ce74cee857a17f97c3be14a205b7db3cdd6de7c4fc3a73a3e220d203",
  "cid": "QmV1e06e6381ce74cee857a17f97c3be14a205b7db3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292654,
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
      "evaluated_at": 1760292654
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
  "sig": "3e38d59b27ac3cf57da76d4c77537d06096217be6cc5e4af0d42d0f8d85aa12b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037779899
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 83027454, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': '90378a324202fffb'}}}