```json
{
  "id": "5dfefe187b3073cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288424,
  "host_pid": "9e6742732c60:1",
  "hash": "6e4ae9a9bbe7fe5a5efeeb593ffa425f1c45630a4a45ae56c7cc32550218dcea",
  "cid": "QmV16e4ae9a9bbe7fe5a5efeeb593ffa425f1c45630a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288424,
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
      "evaluated_at": 1760288424
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
  "sig": "f497cfc7989f7ec3bb6fa80c1d5bae7fbc208be88f780f13575c17a3dce82ac6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 349235110674099
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 15491196, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285763, 'matching_hash': '882aaca4d63a604c'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '349235113', 'validation_error': 'Invalid routing number checksum'}}}