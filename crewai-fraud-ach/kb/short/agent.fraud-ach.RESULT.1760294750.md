```json
{
  "id": "b75b919321bf9b2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294750,
  "host_pid": "9e6742732c60:1",
  "hash": "892d0057da7b31067c954ba1c836fcbeb79b5b536f0225c76e945eb7f6642578",
  "cid": "QmV1892d0057da7b31067c954ba1c836fcbeb79b5b53",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294750,
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
      "evaluated_at": 1760294750
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
  "sig": "b965e862f43d1417dd708d435fed040595db20f597353fa84efacd486f7b4b44"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 701651307465811
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 50772740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '31f29b630ea434da'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}