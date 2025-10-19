```json
{
  "id": "560bc26220079892",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289198,
  "host_pid": "9e6742732c60:1",
  "hash": "a0e3222bb1d790471b20409bbc2c90073bc914890cdb5c0f7d3a25e79d37f071",
  "cid": "QmV1a0e3222bb1d790471b20409bbc2c90073bc91489",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289198,
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
      "evaluated_at": 1760289198
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
  "sig": "b2d053bfa6436e36e88121051a29fb5ec3da9970769769d715e892e1eb1b8c59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031910208
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 44219432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '8397d9ba38a9dfb7'}}}