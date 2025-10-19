```json
{
  "id": "70137881b173ccd3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293941,
  "host_pid": "9e6742732c60:1",
  "hash": "69b43beb1565dfadb8112c761f61de0eb2f617f887a89dd7b9f60ddcd16dd7fb",
  "cid": "QmV169b43beb1565dfadb8112c761f61de0eb2f617f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293941,
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
      "evaluated_at": 1760293941
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
  "sig": "1ea5f9f3852df205d501335be6724a5d5343b07b97d177296e3002cb1557b9e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022683015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 55789320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285765, 'matching_hash': 'a34aa564f21aebc1'}}}