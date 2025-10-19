```json
{
  "id": "b0949d7169aa93c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291838,
  "host_pid": "9e6742732c60:1",
  "hash": "bffe4c7c27b28c5b6f113ab5c70d3ba96ba552f359755c7b8557a95ecf2384d4",
  "cid": "QmV1bffe4c7c27b28c5b6f113ab5c70d3ba96ba552f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291838,
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
      "evaluated_at": 1760291838
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
  "sig": "86a73fa2429411f67e00f212d2962ecd773dcf78e30f53efa7047966153f0b26"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 612898027160979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 21729664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '1a410ec770966ef8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}