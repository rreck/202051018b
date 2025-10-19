```json
{
  "id": "8f23f1d7cd4bb69f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291701,
  "host_pid": "9e6742732c60:1",
  "hash": "310ad0f2b8c6b0b76adf74f6193984d5439a08b43189ef5bd57dab8cbe29d599",
  "cid": "QmV1310ad0f2b8c6b0b76adf74f6193984d5439a08b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291701,
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
      "evaluated_at": 1760291701
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "6b6ed9718002ba55596d4da0ba82a27662cdaec1b8fb75777c76059a193d0b14"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 607486347609576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 79196731, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '01e47067eb24b5e9'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}