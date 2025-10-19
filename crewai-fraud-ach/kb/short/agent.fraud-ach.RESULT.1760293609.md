```json
{
  "id": "7e7109af9445d749",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293609,
  "host_pid": "9e6742732c60:1",
  "hash": "8e492a026612dfc7000a3efc3bb4a11bf4e0f8cec397b1485801ab0c1a32c12e",
  "cid": "QmV18e492a026612dfc7000a3efc3bb4a11bf4e0f8ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293609,
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
      "evaluated_at": 1760293609
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
  "sig": "751c635a53b79330137d5a381d48a9d2db60ad796c336eb5434db18b04b354fc"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 069024451692491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 47268018, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '560f842b4bd5b95e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '069024457', 'validation_error': 'Invalid routing number checksum'}}}