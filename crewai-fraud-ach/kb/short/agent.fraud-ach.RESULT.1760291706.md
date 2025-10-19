```json
{
  "id": "14997e438808795f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291706,
  "host_pid": "9e6742732c60:1",
  "hash": "5e7692f7bcc39c632c3dc36bc54ce7f3bc560c0c10f61e5d592453684a4c3a8e",
  "cid": "QmV15e7692f7bcc39c632c3dc36bc54ce7f3bc560c0c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291706,
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
      "evaluated_at": 1760291707
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
  "sig": "e9292e2c94c5965627826a909ba2182e94754d8638f1a1b2a5408eefea4b6ee6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032200831
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 10499448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285764, 'matching_hash': 'cae8555d53751756'}}}