```json
{
  "id": "27ce50142c13a06a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292793,
  "host_pid": "9e6742732c60:1",
  "hash": "67849fcc5c9b8b0792e62262a96092ea68abc5c7724417839c369b09babc7be7",
  "cid": "QmV167849fcc5c9b8b0792e62262a96092ea68abc5c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292793,
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
      "evaluated_at": 1760292793
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
  "sig": "55c37bc37c31e1d7aa283642edf77ec24c7838ca8a150d036514186d51c99fee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029233033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 85122970, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': 'f6bf3c76ea3935d9'}}}