```json
{
  "id": "f382ac8d5475898d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291430,
  "host_pid": "9e6742732c60:1",
  "hash": "a2ae8ca73b43505d9ec7cf556cd63c7f3c3cfe261cc62a7164d7683c3b297e03",
  "cid": "QmV1a2ae8ca73b43505d9ec7cf556cd63c7f3c3cfe26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291430,
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
      "evaluated_at": 1760291430
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
  "sig": "d6acdffdf1f22cee680b966ee41b8d3f43010166872df48cbc7552399124bbd0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599280040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 85187550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '3242f38050bfb93d'}}}