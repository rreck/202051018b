```json
{
  "id": "1ed0cd37a37c3f42",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286435,
  "host_pid": "9e6742732c60:1",
  "hash": "c6d811edafaadd4077080749564a5b3c4c826f9a0464b4a4f73321b0cfb137a9",
  "cid": "QmV1c6d811edafaadd4077080749564a5b3c4c826f9a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286435,
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
      "evaluated_at": 1760286435
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "7b9488c430aa677e7793b124298a05c5d39b302d41510e759a70dbca2124f5f3"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000246932907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11299400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': 'b5767c7cd6e7c742'}}}