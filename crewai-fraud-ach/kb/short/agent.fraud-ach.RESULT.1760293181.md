```json
{
  "id": "ac97ef412fb2237e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293181,
  "host_pid": "9e6742732c60:1",
  "hash": "e774f0d19e0c67ed40981795d63d7e763c5a9950c36477e0aa350477bd3567b6",
  "cid": "QmV1e774f0d19e0c67ed40981795d63d7e763c5a9950",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293181,
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
      "evaluated_at": 1760293181
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
  "sig": "350c1fa6b37905d8da8aed23b44974005da952dec4b3026b45bcab2115c1b112"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242027891
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 29725215, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285764, 'matching_hash': '176f574fbb51fea2'}}}