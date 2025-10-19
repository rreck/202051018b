```json
{
  "id": "62a61802f70906a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289785,
  "host_pid": "9e6742732c60:1",
  "hash": "bc46091831d75be058768b3794696e75bf60fe501e41bfc3d669c0cb6ca3be0d",
  "cid": "QmV1bc46091831d75be058768b3794696e75bf60fe50",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289785,
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
      "evaluated_at": 1760289785
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
  "sig": "369cb670452527e192a92e653384862c2773bc348dd434cd77a47d3136ab24ef"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 646437634699290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 59577616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': 'd218c468aa26fc36'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}