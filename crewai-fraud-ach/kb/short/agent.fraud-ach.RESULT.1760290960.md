```json
{
  "id": "64fccebc6a7779a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290960,
  "host_pid": "9e6742732c60:1",
  "hash": "2ed39c0f572a661ced3d6dd461d4cf42432bbe7e2ad741680857cf61a292e69f",
  "cid": "QmV12ed39c0f572a661ced3d6dd461d4cf42432bbe7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290960,
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
      "evaluated_at": 1760290960
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
  "sig": "5a4d688c53dde2421c75bfa31ef09a79b2ccef49bbd06f9cc7f581d4840489ea"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 507153179781967
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 34804086, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285765, 'matching_hash': 'b9dbbc4d232307f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '507153176', 'validation_error': 'Invalid routing number checksum'}}}