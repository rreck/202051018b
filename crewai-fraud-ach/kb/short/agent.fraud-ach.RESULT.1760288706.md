```json
{
  "id": "9ed5ee906e368ed4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288706,
  "host_pid": "9e6742732c60:1",
  "hash": "3be5a0e72063fb77773cd13d6fc3261eaf3b223fb3a4331dfc73608ed7cebf1a",
  "cid": "QmV13be5a0e72063fb77773cd13d6fc3261eaf3b223f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288706,
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
      "evaluated_at": 1760288706
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
  "sig": "14d556770f4920225094239b2df98c163a092e5278ea002f48ec0b289b46d911"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 32143048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}