```json
{
  "id": "7ab5774aafa52e37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293343,
  "host_pid": "9e6742732c60:1",
  "hash": "92c558f1388f9250f78d17d33f763b36b5527a4e51f06c1a67dfb82b40b261c1",
  "cid": "QmV192c558f1388f9250f78d17d33f763b36b5527a4e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293343,
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
      "evaluated_at": 1760293343
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
  "sig": "1fa3423fb6f0a43744b897d62aae449845c44c2d255cdd9fe2731b3e8527a48b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594254224
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 26112456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285765, 'matching_hash': 'a2bdc2eb52125893'}}}