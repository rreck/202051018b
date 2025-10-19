```json
{
  "id": "c381d3da20391a5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293527,
  "host_pid": "9e6742732c60:1",
  "hash": "79bbe8cfa35d76a0342bb63facaf07a6a6af840554ec0f607bbb31e26b192d27",
  "cid": "QmV179bbe8cfa35d76a0342bb63facaf07a6a6af8405",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293527,
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
      "evaluated_at": 1760293527
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
  "sig": "ee26a980cf88a5078a08b378f13f2e03dbc52f5c34c0f87dcfb74782cc2e96b5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 033505362547520
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 52251980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '3154a67bf8f8af44'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '033505362', 'validation_error': 'Invalid routing number checksum'}}}