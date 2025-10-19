```json
{
  "id": "9324fd654965448c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294758,
  "host_pid": "9e6742732c60:1",
  "hash": "dc60183e7ab18e7875ce1be445f4836d12eaf366f678e2697d619f5b64e5b358",
  "cid": "QmV1dc60183e7ab18e7875ce1be445f4836d12eaf366",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294758,
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
      "evaluated_at": 1760294758
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
  "sig": "b6ae62ac21ddeb9c1aa92ebbde9a9e8d9981436c880f03408afff0ec068bb2ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021368470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 43491048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': 'a5ef2cf235167f67'}}}