```json
{
  "id": "4f56b1c48c52186e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288236,
  "host_pid": "9e6742732c60:1",
  "hash": "b5b0841c484e36e870b5543c7f1403b862b32dd84fbb21ee01b5ad90484ce2f1",
  "cid": "QmV1b5b0841c484e36e870b5543c7f1403b862b32dd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288236,
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
      "evaluated_at": 1760288236
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
  "sig": "9f75d2087069603d3aecd163336acc6ef298d115f048f85067099c2509dc99ef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593598720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 17612280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285763, 'matching_hash': '553fe68124b88597'}}}