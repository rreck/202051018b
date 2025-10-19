```json
{
  "id": "0cf886222d2847a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294917,
  "host_pid": "9e6742732c60:1",
  "hash": "592006796e5531083b088e25c0cb0a44c3821d4db4f952a57f6ae79875a2add2",
  "cid": "QmV1592006796e5531083b088e25c0cb0a44c3821d4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294917,
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
      "evaluated_at": 1760294917
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
  "sig": "781d71043bde85ddacd1ac549c0077926b4a9001396a9fe82f2b044a9a6a0327"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591752071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 27034644, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': 'afb8628b94bcbefe'}}}}