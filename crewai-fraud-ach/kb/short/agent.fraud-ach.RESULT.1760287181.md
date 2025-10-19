```json
{
  "id": "a55907635d297155",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287181,
  "host_pid": "9e6742732c60:1",
  "hash": "991cec4d4c6197419cf28603fb37368b56b505a282fc143bf3c7772f7ae35c04",
  "cid": "QmV1991cec4d4c6197419cf28603fb37368b56b505a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287181,
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
      "evaluated_at": 1760287181
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
  "sig": "c18bfd773ee747250f85bf96a49f2bc2cf5d65619b460006b036bb1a5e5398a0"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000021988031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 12896217, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285764, 'matching_hash': '88465ad333807d91'}}}