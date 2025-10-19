```json
{
  "id": "29bec1943c2f25f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290095,
  "host_pid": "9e6742732c60:1",
  "hash": "994e73276cb3c5fc46e69ccacd45398f33e188923625e7bbe37194ff73ca303c",
  "cid": "QmV1994e73276cb3c5fc46e69ccacd45398f33e18892",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290095,
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
      "evaluated_at": 1760290095
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
  "sig": "539fe0888373ab86912ae9e7eb7db7bd5d824083d8c9c7276708ee57e5644f0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462125361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 24706161, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285764, 'matching_hash': '410e2c6110d1d339'}}}