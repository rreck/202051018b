```json
{
  "id": "9c9c0ac54dbbcfd1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288932,
  "host_pid": "9e6742732c60:1",
  "hash": "b451984ff951bb848932e7462d9c10816fdd5043b7e9c874e1aa33a9a688a5cb",
  "cid": "QmV1b451984ff951bb848932e7462d9c10816fdd5043",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288932,
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
      "evaluated_at": 1760288932
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
  "sig": "3da73959b8f94c4796401237b602baec46798db702b13a56067ea56f6f6c6e2e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037652029
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 30816072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285765, 'matching_hash': '6ae01c61248929d6'}}}