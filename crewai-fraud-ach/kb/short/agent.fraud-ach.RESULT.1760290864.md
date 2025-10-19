```json
{
  "id": "072e88476d3a0d97",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290864,
  "host_pid": "9e6742732c60:1",
  "hash": "268c5d589a082854b7bfe685b4c1bae8c38e4847368460dad50cca471130541a",
  "cid": "QmV1268c5d589a082854b7bfe685b4c1bae8c38e4847",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290864,
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
      "evaluated_at": 1760290864
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
  "sig": "015bb23a4a19eaf741384d16827b9546db2c9c0804aab7e023d5ac013d64e8d1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270776467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 78711612, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}