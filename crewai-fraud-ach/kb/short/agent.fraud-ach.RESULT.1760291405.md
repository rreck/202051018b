```json
{
  "id": "6ffba841f5bb9a16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291405,
  "host_pid": "9e6742732c60:1",
  "hash": "daa8904b3db725ebc505491b42431b935fbebb42aa15a1a9389c95922e026c00",
  "cid": "QmV1daa8904b3db725ebc505491b42431b935fbebb42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291405,
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
      "evaluated_at": 1760291405
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
  "sig": "9abe814d7463582a80f0d1882198b5fa6c482058f6c7a1179bcc2a4109736f73"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276997857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 82779978, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': 'b73e9a6de72cc131'}}}