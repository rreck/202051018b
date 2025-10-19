```json
{
  "id": "8cdca156ceda2094",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293413,
  "host_pid": "9e6742732c60:1",
  "hash": "879d9be1a9e83aa0a14e2f730599ceb049971d052b501d1c38cbe94172a2fd3e",
  "cid": "QmV1879d9be1a9e83aa0a14e2f730599ceb049971d05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293413,
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
      "evaluated_at": 1760293413
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
  "sig": "fbea11acfe394e8edd70b73c62ebe910421b27333db89c63567d0b70118deff7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 020899457068496
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 85982034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285764, 'matching_hash': '41b228ccdaf61559'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '020899456', 'validation_error': 'Invalid routing number checksum'}}}