```json
{
  "id": "3709d10ba28c231a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289398,
  "host_pid": "9e6742732c60:1",
  "hash": "2eecd65f972816c699ddddde5ed0f06540b9caf0688e17e1d6a84018ff2a3962",
  "cid": "QmV12eecd65f972816c699ddddde5ed0f06540b9caf0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289398,
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
      "evaluated_at": 1760289398
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
  "sig": "e9224ff1127a6cfb14ff06c0b96aa5e33e1e1c590df0b7323ab9076c89722217"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 164661958921180
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 28565446, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '1848c81652336fb1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '164661952', 'validation_error': 'Invalid routing number checksum'}}}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}