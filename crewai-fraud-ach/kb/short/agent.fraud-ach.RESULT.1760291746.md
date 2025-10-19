```json
{
  "id": "0283f22c23b6003c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291746,
  "host_pid": "9e6742732c60:1",
  "hash": "c09c92b7405960c1a96db0827a53c8db6c8507723dbb5b53ea48b009f54fe766",
  "cid": "QmV1c09c92b7405960c1a96db0827a53c8db6c850772",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291746,
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
      "evaluated_at": 1760291746
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
  "sig": "4a739cd27f3e01ba0a66299e6627fd2f8bace58f1545083ae20b0594e61b3733"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245112669
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 14667562, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285764, 'matching_hash': '067804ada8f7cd8c'}}}