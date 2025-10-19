```json
{
  "id": "58fc7989e6eceb14",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290676,
  "host_pid": "9e6742732c60:1",
  "hash": "840685446fdcd2ac7824831ea66cfff7cc26d8da833084c5586dfe5b2fb18f64",
  "cid": "QmV1840685446fdcd2ac7824831ea66cfff7cc26d8da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290676,
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
      "evaluated_at": 1760290676
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
  "sig": "388ebdae8d554a381a57e3133ac2f7c392d4e362cbae61a00cda063575cfd4df"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 211815510392855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 52826124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285765, 'matching_hash': '64b36e7650337f92'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '211815514', 'validation_error': 'Invalid routing number checksum'}}}