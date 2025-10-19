```json
{
  "id": "47195f5c31821406",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288142,
  "host_pid": "9e6742732c60:1",
  "hash": "fcc669a4b21a4ce3682846d829e7f4efdcc2f1aa27e9a5ec65aaf87bdfe8534c",
  "cid": "QmV1fcc669a4b21a4ce3682846d829e7f4efdcc2f1aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288142,
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
      "evaluated_at": 1760288142
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
  "sig": "51b06b815a9c8a4b089d069bda0b7535e76db8de6c4dee8392859aa79517bf04"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465723283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 35913276, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285764, 'matching_hash': 'e1350af409930159'}}}