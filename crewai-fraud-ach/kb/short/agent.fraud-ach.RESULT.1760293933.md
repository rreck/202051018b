```json
{
  "id": "726c1e8c24afbdb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293933,
  "host_pid": "9e6742732c60:1",
  "hash": "9313940908dc1b47338883b11b0fe608aa00fe6c36c0671ee5683162b792e46c",
  "cid": "QmV19313940908dc1b47338883b11b0fe608aa00fe6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293933,
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
      "evaluated_at": 1760293933
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
  "sig": "a2c2d7ad10976dbf4e1dc214db0a837da25fd23c61e46d2b6e362790229dcdb7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037423947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 45531828, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': '5528b0ca47a44e30'}}}