```json
{
  "id": "f7a8ee8e46769ca9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294404,
  "host_pid": "9e6742732c60:1",
  "hash": "b09b449ba484cd1081cccb922c3fb301376da36ee9e6e95cea36612188ae34d4",
  "cid": "QmV1b09b449ba484cd1081cccb922c3fb301376da36e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294404,
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
      "evaluated_at": 1760294404
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
  "sig": "7b4bc84e24346941a7ebfac94c75a76777d50f092469e7f53bd06b5a3f6060b9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596687644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 24082281, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'eb3c042d8ede64d4'}}}