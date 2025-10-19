```json
{
  "id": "f30b64a7cd647b55",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290328,
  "host_pid": "9e6742732c60:1",
  "hash": "3ef689b91194809960c9d73809e75e27659bc69e960f708517104b7dd89e762e",
  "cid": "QmV13ef689b91194809960c9d73809e75e27659bc69e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290328,
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
      "evaluated_at": 1760290328
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
  "sig": "262746629de301782ca3ac58da871fc4efbebd44f7748e286f21eb7d105d7fc1"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 107455396447712
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 73082226, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285765, 'matching_hash': 'bb26c320d6c9a382'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '107455391', 'validation_error': 'Invalid routing number checksum'}}}