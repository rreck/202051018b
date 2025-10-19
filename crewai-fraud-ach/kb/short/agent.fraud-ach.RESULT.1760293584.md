```json
{
  "id": "bb0bae4fa1464ea2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293584,
  "host_pid": "9e6742732c60:1",
  "hash": "958c8ca5d7cb5cc7e9949a662b94e8f0540978d52dbb2da9629c1cc9081951f7",
  "cid": "QmV1958c8ca5d7cb5cc7e9949a662b94e8f0540978d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293584,
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
      "evaluated_at": 1760293584
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
  "sig": "3b64580d8cb82dfa3347fcf58904f88cea68df02550f9fb33e07ec6a51b65806"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154024479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 70477121, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285765, 'matching_hash': 'af946edf21c4a5d6'}}}