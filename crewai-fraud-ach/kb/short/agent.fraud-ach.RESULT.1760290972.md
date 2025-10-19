```json
{
  "id": "e9df8a67f0a8adb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290972,
  "host_pid": "9e6742732c60:1",
  "hash": "fd692744a305c8fea99dbbc088c65ba6cf2c8bc75532f5655ae8774881527a12",
  "cid": "QmV1fd692744a305c8fea99dbbc088c65ba6cf2c8bc7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290972,
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
      "evaluated_at": 1760290972
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "1e035fa958788c5778201cebcfd19a67a15cf4d2d8fa4c8e0d8f5ef2d55ee926"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596004100
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 26046644, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '0723803785cdf871'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '294015854', 'validation_error': 'Invalid routing number checksum'}}}