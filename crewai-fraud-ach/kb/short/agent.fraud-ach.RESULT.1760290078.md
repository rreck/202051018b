```json
{
  "id": "2ea562579e4105d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290078,
  "host_pid": "9e6742732c60:1",
  "hash": "d25411a1082b96febd9c03513c75365f99ee6213c441ac6a6f99a7d04a550a69",
  "cid": "QmV1d25411a1082b96febd9c03513c75365f99ee6213",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290078,
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
      "evaluated_at": 1760290078
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
  "sig": "b591893168f64c228d01759fe63b1080784db863a84b35ddb6acad15b03985be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279336195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 56958642, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': 'bc4c468b17fbec63'}}}