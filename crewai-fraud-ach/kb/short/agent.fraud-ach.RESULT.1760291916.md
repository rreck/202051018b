```json
{
  "id": "70214ab264c3108e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291916,
  "host_pid": "9e6742732c60:1",
  "hash": "7283ffe0816b6fdc36007c161029d075214e9503db61f7c6133fd0b0006c6883",
  "cid": "QmV17283ffe0816b6fdc36007c161029d075214e9503",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291916,
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
      "evaluated_at": 1760291916
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
  "sig": "a43045c4dd5897ee9337a1517cdb358d857a9b99afc275d16b14fe818b956d6f"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 498752223480159
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 73245498, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': '492624c5b9a9c8c0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '498752220', 'validation_error': 'Invalid routing number checksum'}}}