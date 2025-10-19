```json
{
  "id": "03137b4bffdcd580",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291933,
  "host_pid": "9e6742732c60:1",
  "hash": "f63e29cd02b5950948f0013f0fcd3bec67ace0ba23427b654d43be876e76ae5d",
  "cid": "QmV1f63e29cd02b5950948f0013f0fcd3bec67ace0ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291933,
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
      "evaluated_at": 1760291933
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
  "sig": "6a560869416f912a35595fe85b2d1b7e0ac19db3cc27477b963603c6943f378b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248025724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 21088308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285764, 'matching_hash': 'cc12810353983743'}}}