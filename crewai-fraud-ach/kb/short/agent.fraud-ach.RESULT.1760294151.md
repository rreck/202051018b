```json
{
  "id": "01bbb07add044d40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294151,
  "host_pid": "9e6742732c60:1",
  "hash": "519c2fa4bea7dcffb87ecaadc9550768732f85c5a6a18cbc6806f62dbdc0ae67",
  "cid": "QmV1519c2fa4bea7dcffb87ecaadc9550768732f85c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294151,
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
      "evaluated_at": 1760294151
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
  "sig": "7efcbc89edac0cbc061b1db364bd1eb34123476ea9fd796968704e73e1d6e003"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 507153179781967
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 49537104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': 'b9dbbc4d232307f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '507153176', 'validation_error': 'Invalid routing number checksum'}}}