```json
{
  "id": "0336914a9ab734e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291079,
  "host_pid": "9e6742732c60:1",
  "hash": "bb1b61094b7c736d07c5993c056fe8a2dd0495dccd449f1233ff3348aa649c60",
  "cid": "QmV1bb1b61094b7c736d07c5993c056fe8a2dd0495dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291079,
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
      "evaluated_at": 1760291079
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
  "sig": "cc052e7061eff864dc9bd9ab40193810d25496a18f670c08b198e9809c6655f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 55515048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}