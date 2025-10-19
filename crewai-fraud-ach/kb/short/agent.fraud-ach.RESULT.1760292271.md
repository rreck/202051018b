```json
{
  "id": "a92a88b7165c8890",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292271,
  "host_pid": "9e6742732c60:1",
  "hash": "942e3ee12e0bd7e465a1e52de80cdc73b51cd45f1732fdf191584511cdfd2398",
  "cid": "QmV1942e3ee12e0bd7e465a1e52de80cdc73b51cd45f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292271,
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
      "evaluated_at": 1760292271
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
  "sig": "c1d3bddc435504926c974dc0011091a837c6bc005f25a64d0e2fe64a014e8016"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591167362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 60541968, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '24df3db171a5add1'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}