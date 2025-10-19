```json
{
  "id": "2c2b8482fac2ddd9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293282,
  "host_pid": "9e6742732c60:1",
  "hash": "5bd63d66ed928e2f1fd40601dd7f4e21cadc295f75dadd9f078170da5a0746fb",
  "cid": "QmV15bd63d66ed928e2f1fd40601dd7f4e21cadc295f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293282,
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
      "evaluated_at": 1760293282
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
  "sig": "b46994a29bbf0e925f1de815c12462eee9ea2ecb94e01e726452b843659706de"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 906924177607497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 55468065, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285765, 'matching_hash': 'a0bedab775ea6194'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '906924178', 'validation_error': 'Invalid routing number checksum'}}}