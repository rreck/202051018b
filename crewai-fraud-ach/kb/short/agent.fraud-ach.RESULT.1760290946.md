```json
{
  "id": "f41221bdfd7483fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290946,
  "host_pid": "9e6742732c60:1",
  "hash": "625099735b235a2616d1214b84997e05d74cb45e065d81dd447a2fd5f31f8c3c",
  "cid": "QmV1625099735b235a2616d1214b84997e05d74cb45e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290946,
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
      "evaluated_at": 1760290946
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
  "sig": "9b9d34023ca82db618e994b3d1bc5178d3b642fe9e21be121bda1e73a226e70d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465603072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'e359f7b1cd5a9343'}}}een': 1760285763, 'matching_hash': 'b54d2b84a0558fd6'}}}