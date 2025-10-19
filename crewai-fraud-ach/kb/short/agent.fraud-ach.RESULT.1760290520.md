```json
{
  "id": "f18b6eadbc9cc5dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290520,
  "host_pid": "9e6742732c60:1",
  "hash": "a358b194384827cf78fbfbb704f107a65425b32db59ee0d916f0495df51a4946",
  "cid": "QmV1a358b194384827cf78fbfbb704f107a65425b32d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290520,
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
      "evaluated_at": 1760290520
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
  "sig": "c89a5aa65f02ead2d05d5e42882d93f08819ec70ceccaf53bb84e4a4a54efcee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 26697280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}