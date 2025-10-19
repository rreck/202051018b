```json
{
  "id": "d2f837a06935c662",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289533,
  "host_pid": "9e6742732c60:1",
  "hash": "ba21caa95a82598cc2031f42d63bddce4ed57e8c9e8194b08ffad053c15cfe1d",
  "cid": "QmV1ba21caa95a82598cc2031f42d63bddce4ed57e8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289533,
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
      "evaluated_at": 1760289533
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
  "sig": "65963c746e5dcf73fddfa13d4a175bae3a1afc33471ce01b63939298c4ece2ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596116036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 31500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': 'e2bf4d89584c6445'}}}