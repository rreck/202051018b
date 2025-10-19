```json
{
  "id": "9beb71d589807e58",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287930,
  "host_pid": "9e6742732c60:1",
  "hash": "38652ed62e89f28d6cc0139da82efa3e3dd2580db585902280dd329caeb40b03",
  "cid": "QmV138652ed62e89f28d6cc0139da82efa3e3dd2580d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287930,
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
      "evaluated_at": 1760287930
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
  "sig": "a7c69aecdfc1453f5d4bc748665506d28624c4b7c2698b942817f782215b2aaf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590136300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 38147879, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285764, 'matching_hash': '2d6fc2065b3c1287'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}