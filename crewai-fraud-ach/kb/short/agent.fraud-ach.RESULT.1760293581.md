```json
{
  "id": "2e048b13b4e4b229",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293581,
  "host_pid": "9e6742732c60:1",
  "hash": "9e91d99af98bd8740bbd21f1a4b0cc3f27342de4bf8f0102173378049f1163ce",
  "cid": "QmV19e91d99af98bd8740bbd21f1a4b0cc3f27342de4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293581,
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
      "evaluated_at": 1760293581
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
  "sig": "14e6a7cdc8e7ce073c2ade7e1a4c1cea4c2a546f848aef78464b6f1798049ac6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 479377306721842
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 72187882, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285764, 'matching_hash': '9b6eff4280210a62'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '479377304', 'validation_error': 'Invalid routing number checksum'}}}