```json
{
  "id": "4937bb00d3bcc9dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292901,
  "host_pid": "9e6742732c60:1",
  "hash": "81ec98468a81b3f1b604f4212ae68e96e3070aada0e2b483293b790892a1e2a9",
  "cid": "QmV181ec98468a81b3f1b604f4212ae68e96e3070aad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292901,
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
      "evaluated_at": 1760292901
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
  "sig": "6cd5e1ecdfc1318ef617e4efb9d0d01c74c622042d0e9190b69dc419f83dcba4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243187094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 92817765, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285764, 'matching_hash': '46900333a68fa7ba'}}}