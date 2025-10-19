```json
{
  "id": "622ae7234bedbfa5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286752,
  "host_pid": "9e6742732c60:1",
  "hash": "f8428c04a44c15dcb9bd38646e8a57395083673a09b5af11fde3018b7db40a2e",
  "cid": "QmV1f8428c04a44c15dcb9bd38646e8a57395083673a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286752,
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
      "evaluated_at": 1760286752
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "208da856388ab94c4523d7dfcfbc8e92a0cf9c37140e042e92c2be53086029f8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009592795708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16547436, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285763, 'matching_hash': '6f9672c314113419'}}}