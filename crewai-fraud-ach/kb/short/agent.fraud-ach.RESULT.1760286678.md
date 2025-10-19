```json
{
  "id": "fdcb07050756b8e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286678,
  "host_pid": "9e6742732c60:1",
  "hash": "6aaf99def6293d19ec5858e9adce92b383c92a89b5bea95ee27d59926d9943bf",
  "cid": "QmV16aaf99def6293d19ec5858e9adce92b383c92a89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286678,
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
      "evaluated_at": 1760286678
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
  "sig": "9efbb04ab9bf81fee14446bf0ffe3f32e1768b887262db7fdc20a8cc5c847e6f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009590866940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14024868, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}