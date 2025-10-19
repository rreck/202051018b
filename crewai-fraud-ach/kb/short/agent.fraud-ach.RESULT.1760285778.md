```json
{
  "id": "009c1b1dd1400eda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285778,
  "host_pid": "9e6742732c60:1",
  "hash": "552f2e916de271afa290adb0841b563b43503b41d688c87f8406940f66dadaaf",
  "cid": "QmV1552f2e916de271afa290adb0841b563b43503b41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285778,
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
      "evaluated_at": 1760285778
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
  "sig": "db9b970055f7513067527fbe3612b998e3357bfd21304390360d5a2fe452a3ff"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009591602283
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285763, 'matching_hash': '995d19d96715feaf'}}}