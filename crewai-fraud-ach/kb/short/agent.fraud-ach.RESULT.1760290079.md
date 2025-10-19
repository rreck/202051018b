```json
{
  "id": "32de481d3a02f716",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290079,
  "host_pid": "9e6742732c60:1",
  "hash": "55a10907f6baf39a0fb0849c66f94643d9fb6fc60d652c680cb9d58a44ebb9a8",
  "cid": "QmV155a10907f6baf39a0fb0849c66f94643d9fb6fc6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290079,
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
      "evaluated_at": 1760290079
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
  "sig": "6f738f003be3b94d098ef48ba61c8ab0225389eceff5149689ebe3468f4640a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038197650
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 26517447, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': '1b9150809eb731a5'}}}