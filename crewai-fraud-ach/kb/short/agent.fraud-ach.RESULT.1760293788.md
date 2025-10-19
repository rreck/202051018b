```json
{
  "id": "c8afbfec42bceec7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293788,
  "host_pid": "9e6742732c60:1",
  "hash": "50be7ac78dd3dcf9c94f5ccda92bfc7605e19e7c1b1f9f1521b458f70bb2cc2a",
  "cid": "QmV150be7ac78dd3dcf9c94f5ccda92bfc7605e19e7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293788,
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
      "evaluated_at": 1760293788
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
  "sig": "3c932f98671cbab948024c1e6b25186ddbef6a9224f3a220c6d5550045730deb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033965137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 32103000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': 'a94abbf708458614'}}}