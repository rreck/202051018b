```json
{
  "id": "fd26d148cfcf4ac7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290427,
  "host_pid": "9e6742732c60:1",
  "hash": "b58e4fce5ee91cfb53c3b4fe926bc038ab5763f80b09ac4b9ee1f36bc46ae42a",
  "cid": "QmV1b58e4fce5ee91cfb53c3b4fe926bc038ab5763f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290427,
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
      "evaluated_at": 1760290427
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
  "sig": "35e0fd17e1324fdf6c951686514f57abcb55277ce6697c9170cf14e146854be4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271528987
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 61052250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': '52a7e62e45a672d0'}}}