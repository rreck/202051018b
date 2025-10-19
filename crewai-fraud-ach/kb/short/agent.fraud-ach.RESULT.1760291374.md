```json
{
  "id": "5f21ad7d06b80fae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291374,
  "host_pid": "9e6742732c60:1",
  "hash": "d315e084ee360e27e68d7ff3f009ec0e4b21cf26c9a30d02c5a5de8f86e3ff4d",
  "cid": "QmV1d315e084ee360e27e68d7ff3f009ec0e4b21cf26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291374,
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
      "evaluated_at": 1760291374
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
  "sig": "02528dba222451ecea604b843fea00ef52a1029a08d43484795d030b06ce6cd5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463882943
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 21453384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}