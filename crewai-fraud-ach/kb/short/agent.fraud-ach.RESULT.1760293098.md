```json
{
  "id": "19ce372d56122cd8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293098,
  "host_pid": "9e6742732c60:1",
  "hash": "ea6bb25cd87c9495e8b50b65d214cc581d5ac3c311d4ae5bc51122758c924829",
  "cid": "QmV1ea6bb25cd87c9495e8b50b65d214cc581d5ac3c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293098,
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
      "evaluated_at": 1760293098
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
  "sig": "0ade92c8645e5746c4d45b89d177050595696ac08e2c16365a9e6f6fb1439d13"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 589241761167275
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 66172554, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285765, 'matching_hash': 'a1dced1ef969015f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '589241760', 'validation_error': 'Invalid routing number checksum'}}}