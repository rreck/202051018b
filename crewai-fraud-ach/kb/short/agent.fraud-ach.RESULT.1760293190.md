```json
{
  "id": "30697c8874b178bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293190,
  "host_pid": "9e6742732c60:1",
  "hash": "981c772b490fe2c0a1c1f3ba7dd96df526bfeb759dab931028d686bca74bcffa",
  "cid": "QmV1981c772b490fe2c0a1c1f3ba7dd96df526bfeb75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293190,
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
      "evaluated_at": 1760293190
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
  "sig": "397b052d059d4343d744d8ad7d3cb07f4c5c0846f3d6184751286703efc3b923"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279234721
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 49077756, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285764, 'matching_hash': 'a4a7a8ef6540eadb'}}}