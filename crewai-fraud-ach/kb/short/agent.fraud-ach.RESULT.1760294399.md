```json
{
  "id": "358a1ace917f2f1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294399,
  "host_pid": "9e6742732c60:1",
  "hash": "cada3ca5ae52fcc0ec9303e4ddb2aa3a3d885930bae139700608f49644ccabe4",
  "cid": "QmV1cada3ca5ae52fcc0ec9303e4ddb2aa3a3d885930",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294399,
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
      "evaluated_at": 1760294399
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
  "sig": "bbc41b253326db65d19a67df0b0fe4cbd98e34b4300a62be172712f142c10f94"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 818309298369568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 111653070, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': '9e3984c977816ea5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}