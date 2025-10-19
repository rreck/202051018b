```json
{
  "id": "6c8487d3b17eddaf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290777,
  "host_pid": "9e6742732c60:1",
  "hash": "8d41bac7f0f4905a59968b6daca42bc86991161b312e4913fd9677be0b08b07c",
  "cid": "QmV18d41bac7f0f4905a59968b6daca42bc86991161b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290777,
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
      "evaluated_at": 1760290777
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
  "sig": "13ca5646c6662c4866972d09529a73729cb70f249b8b964ab961c66785d3da2c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 304701772219564
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 38004975, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285764, 'matching_hash': '19ec134c2c5b9271'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '304701776', 'validation_error': 'Invalid routing number checksum'}}}