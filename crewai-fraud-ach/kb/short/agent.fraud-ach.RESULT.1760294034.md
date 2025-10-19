```json
{
  "id": "56df563d04954bfb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294034,
  "host_pid": "9e6742732c60:1",
  "hash": "f9e63595731e6fce0a191156a16f492232f34af8f2d4e243d5d7c718513a3420",
  "cid": "QmV1f9e63595731e6fce0a191156a16f492232f34af8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294034,
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
      "evaluated_at": 1760294034
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
  "sig": "3bc50e33e122e3a9596fc1d3cde97fbcb126fa238e147632d2de4a780da4026e"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 033505362547520
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 54627070, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '3154a67bf8f8af44'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '033505362', 'validation_error': 'Invalid routing number checksum'}}}