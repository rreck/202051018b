```json
{
  "id": "a2f24a91d4423c69",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293361,
  "host_pid": "9e6742732c60:1",
  "hash": "5928eb67e412e54676e11d1d1e6c8c639f1e82288ba6bb269040b1d015bf9698",
  "cid": "QmV15928eb67e412e54676e11d1d1e6c8c639f1e8228",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293361,
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
      "evaluated_at": 1760293361
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
  "sig": "5b35430295646e30f0a426c9d8fa49daf6dc1b3a6f98098678ecce115ba90a4e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022330150
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 95623220, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': 'b30e2736c805251a'}}}