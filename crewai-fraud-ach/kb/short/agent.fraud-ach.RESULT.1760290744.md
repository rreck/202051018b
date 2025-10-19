```json
{
  "id": "ebe0cfe7541b154f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290744,
  "host_pid": "9e6742732c60:1",
  "hash": "0f57432db2cbd870cc70a736ab608b967a66e46be844707d143ae99528c2c4f1",
  "cid": "QmV10f57432db2cbd870cc70a736ab608b967a66e46b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290744,
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
      "evaluated_at": 1760290744
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
  "sig": "4d5e2bf5c6352d73c0343e36c594b4403ad18690edfeffe96b417291654b810e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 56997552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}