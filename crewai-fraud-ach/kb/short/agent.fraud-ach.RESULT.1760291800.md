```json
{
  "id": "c51ddf4658e790fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291800,
  "host_pid": "9e6742732c60:1",
  "hash": "90d4ebdc66ed298211b30db8dc98e8500624353d28b8ad9305a949917ceca10b",
  "cid": "QmV190d4ebdc66ed298211b30db8dc98e8500624353d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291800,
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
      "evaluated_at": 1760291800
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
  "sig": "2e517cb0bf002e9d221df6842dc399a9ebce12f353c50cf4ed31f28baa42ebf9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 478694940117269
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 35432460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285764, 'matching_hash': 'c8ebc968ccc74844'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '478694940', 'validation_error': 'Invalid routing number checksum'}}}