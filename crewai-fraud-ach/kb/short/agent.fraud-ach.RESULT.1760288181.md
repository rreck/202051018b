```json
{
  "id": "5fb95a010cd7522d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288181,
  "host_pid": "9e6742732c60:1",
  "hash": "dfd016c018ebb92b6a8b5901dcd3d1262211f874671ae78f70e100c9d0c455a6",
  "cid": "QmV1dfd016c018ebb92b6a8b5901dcd3d1262211f874",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288181,
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
      "evaluated_at": 1760288181
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
  "sig": "2f3eaf146c964d0c101584aa69e147d67fcc56b38c4179f618f847eca1779222"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 25226725, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}