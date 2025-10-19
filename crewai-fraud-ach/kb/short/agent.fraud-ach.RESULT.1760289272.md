```json
{
  "id": "54c6ce7f5da9abe5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289272,
  "host_pid": "9e6742732c60:1",
  "hash": "3d8c9a96c4ca586afe9137ae8b108bbfbb5ab3e757bb07c211bfca8b5bf3d2e5",
  "cid": "QmV13d8c9a96c4ca586afe9137ae8b108bbfbb5ab3e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289272,
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
      "evaluated_at": 1760289272
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
  "sig": "c2e8c8ef3a198bc03e7e648c82a38765dfb2abfb241c7dd384ee181d532fa46a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025824799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 30709736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285765, 'matching_hash': 'f20c8e7a7a7e0174'}}}