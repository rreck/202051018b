```json
{
  "id": "a3bea749b6f8c627",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293475,
  "host_pid": "9e6742732c60:1",
  "hash": "9a802860d3a2510a1e55e306ed544aeeeb7196115dd6794631cc4545cbc44ddc",
  "cid": "QmV19a802860d3a2510a1e55e306ed544aeeeb719611",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293475,
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
      "evaluated_at": 1760293476
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
  "sig": "84df818d64c815da34e7abde423be826c54a5b9aa7548b6fc88df9c4c517984b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 000042122595756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 295, 'threshold': 50, 'total_amount': 116458920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 294, 'first_seen': 1760284979, 'matching_hash': 'f607cf2148e042a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '000042121', 'validation_error': 'Invalid routing number checksum'}}}