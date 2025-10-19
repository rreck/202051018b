```json
{
  "id": "517bbe52cddaa632",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287007,
  "host_pid": "9e6742732c60:1",
  "hash": "aaabfe0ddccd343457d133157d8f3b2c6555f10c5e7996035d35f2cde8039188",
  "cid": "QmV1aaabfe0ddccd343457d133157d8f3b2c6555f10c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287007,
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
      "evaluated_at": 1760287008
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
  "sig": "4c84326f0dbe32c3a94542b98b9cfe7f089cb7ef20f62496c962b1833479ffe8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156237747
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285763, 'matching_hash': 'b60e159429465bd2'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285763, 'matching_hash': 'b939c4c4097f2f1f'}}}