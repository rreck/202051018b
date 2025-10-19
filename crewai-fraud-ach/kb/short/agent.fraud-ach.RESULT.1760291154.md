```json
{
  "id": "f13aa9d948c574d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291154,
  "host_pid": "9e6742732c60:1",
  "hash": "d6512d68e3cdcc4c81f4c714c813e521501065682c26e92c124cae5357cc16ba",
  "cid": "QmV1d6512d68e3cdcc4c81f4c714c813e52150106568",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291154,
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
      "evaluated_at": 1760291154
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
  "sig": "bb826bd6a94a148de779421d0b56ba3856c21718f07773534bb00d55ff5a25be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157375662
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 24066940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760284979, 'matching_hash': '8218a7a652f8297c'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}