```json
{
  "id": "79e3decdeab6952b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292408,
  "host_pid": "9e6742732c60:1",
  "hash": "5f57f6f75ddc242d188babcc3a388f1e8b7a32037ed97be95f6e96f28bf185dd",
  "cid": "QmV15f57f6f75ddc242d188babcc3a388f1e8b7a3203",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292408,
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
      "evaluated_at": 1760292408
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
  "sig": "649c3ab56e74e4ebe155a731da95106b4298a41ac49b217348c5397d246804b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039326834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 50450912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': '4e66e6716d66a614'}}}