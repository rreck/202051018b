```json
{
  "id": "dcfdad9724b754e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288633,
  "host_pid": "9e6742732c60:1",
  "hash": "63d8391abd283b471ad7011e72776c12fb2df4cfe2472b784847c7d1658af0b3",
  "cid": "QmV163d8391abd283b471ad7011e72776c12fb2df4cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288633,
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
      "evaluated_at": 1760288633
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
  "sig": "f6c5218e43eea39607719e452033f0f98b36f99a14d6960b63a5adee7b412f3d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 683146203883533
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 36869778, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285764, 'matching_hash': '8f404d0fc37310f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '683146208', 'validation_error': 'Invalid routing number checksum'}}}