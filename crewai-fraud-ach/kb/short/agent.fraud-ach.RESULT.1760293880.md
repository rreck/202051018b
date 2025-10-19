```json
{
  "id": "e80fa3c8527d3585",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293880,
  "host_pid": "9e6742732c60:1",
  "hash": "b4235d53cd57378a19a4f7c836314d78239353b462c96de2bae2b14ec4bad73b",
  "cid": "QmV1b4235d53cd57378a19a4f7c836314d78239353b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293880,
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
      "evaluated_at": 1760293880
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
  "sig": "d65e24fea8207752a7be2770de6196874d6cf206f2a1ccc74148940c1cd01554"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279970164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 41916004, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': 'dc8a7598801f2a18'}}}