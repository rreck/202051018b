```json
{
  "id": "6b8e5fc5be2ac265",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290899,
  "host_pid": "9e6742732c60:1",
  "hash": "ca6a34ae466876c5ed11b9305a5ea87e98efbc1183564a4463fc9804f06826f9",
  "cid": "QmV1ca6a34ae466876c5ed11b9305a5ea87e98efbc11",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290899,
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
      "evaluated_at": 1760290899
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
  "sig": "f0dcce00b50340fb682c65c95306ff351864e673cef7811f754a897b063e1f94"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 304701772219564
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 38722050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285764, 'matching_hash': '19ec134c2c5b9271'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '304701776', 'validation_error': 'Invalid routing number checksum'}}}