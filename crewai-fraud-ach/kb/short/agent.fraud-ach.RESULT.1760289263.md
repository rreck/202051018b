```json
{
  "id": "b8fe23bf96ba1178",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289263,
  "host_pid": "9e6742732c60:1",
  "hash": "0f226a1f8660270b8f0ac3e3df08ee6849a374f6081b52d5f186430163aac369",
  "cid": "QmV10f226a1f8660270b8f0ac3e3df08ee6849a374f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289263,
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
      "evaluated_at": 1760289263
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
  "sig": "654ca421349dc5c0ad978937808592d76e7e983e28fff7dc9ab9c62524225152"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 612898027160979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 13935328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': '1a410ec770966ef8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}