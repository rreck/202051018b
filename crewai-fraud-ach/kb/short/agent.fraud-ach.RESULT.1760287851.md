```json
{
  "id": "42c79b17ce8e6db0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287851,
  "host_pid": "9e6742732c60:1",
  "hash": "946f84944bf95ac281d90c5c5ab180902c553c5e6931facb7a0f88e41b4197c9",
  "cid": "QmV1946f84944bf95ac281d90c5c5ab180902c553c5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287851,
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
      "evaluated_at": 1760287851
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
  "sig": "9bd14c636d946c5e2311be87fbda5e44722efa756f1d2ffbf6f132ca1c6adb1a"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 026009597862857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 14786828, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285765, 'matching_hash': 'eac3ff1003c03af8'}}}