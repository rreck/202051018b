```json
{
  "id": "b27bd8369ee0a0ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292205,
  "host_pid": "9e6742732c60:1",
  "hash": "13df121ea9e866bb4395786f3789322ac5ed0708bac055279a0b546b76a300c2",
  "cid": "QmV113df121ea9e866bb4395786f3789322ac5ed0708",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292205,
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
      "evaluated_at": 1760292205
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
  "sig": "24ead94a27aa242968e670d6b7ca57b1b05d3de88e148e4868590647fb4e57eb"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 845955323982908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 69303168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285765, 'matching_hash': '603efe89834eadf7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '845955329', 'validation_error': 'Invalid routing number checksum'}}}