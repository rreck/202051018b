```json
{
  "id": "417c229b3d19af8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288893,
  "host_pid": "9e6742732c60:1",
  "hash": "6a32933868ab28050611094d4e4b142e6c74bb73778d150c12d78dc787d7e441",
  "cid": "QmV16a32933868ab28050611094d4e4b142e6c74bb73",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288893,
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
      "evaluated_at": 1760288893
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
  "sig": "69f6c3f335950c878702d98a98ad45048e6dad8dfd9f746460f4e28431874e6c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 870312149939109
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 42699099, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285765, 'matching_hash': '2dbf2bb6cc4c52b4'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}