```json
{
  "id": "a9c492e8ce8ca2cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293522,
  "host_pid": "9e6742732c60:1",
  "hash": "75e9b1b53bdc128eda53aad708f8ec0f3585435bf377a6d85293d203d930ea68",
  "cid": "QmV175e9b1b53bdc128eda53aad708f8ec0f3585435b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293522,
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
      "evaluated_at": 1760293522
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
  "sig": "50017d565bd7ac09808e4637f94458c006c1081e22187b5945771131de13f56d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244291071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 27847820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '1f8fb3dc368ee7c3'}}}