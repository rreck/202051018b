```json
{
  "id": "c151a1791cd7d42d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286522,
  "host_pid": "9e6742732c60:1",
  "hash": "643e6f696609459de5a647508a4e3c5476cb7d75abdecc18428cc9c4589259d6",
  "cid": "QmV1643e6f696609459de5a647508a4e3c5476cb7d75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286522,
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
      "evaluated_at": 1760286522
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
  "sig": "31d177cddffb4c954d55e174092970ecbcc1ce7ad4bcf17bd1de3bbe0003c734"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009592426992
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11949756, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285763, 'matching_hash': '6c96fa15a49bffda'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '051442869', 'validation_error': 'Invalid routing number checksum'}}}