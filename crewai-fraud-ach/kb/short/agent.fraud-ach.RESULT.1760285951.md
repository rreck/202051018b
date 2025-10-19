```json
{
  "id": "838bd938767bc9ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285951,
  "host_pid": "9e6742732c60:1",
  "hash": "1954e14db6b8ff8d8938ac33e76cd15675e325871a25374f3f69e02ecea3e04e",
  "cid": "QmV11954e14db6b8ff8d8938ac33e76cd15675e32587",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285951,
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
      "evaluated_at": 1760285951
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
  "sig": "ca13f425c23a6478f0330b85397b2664b466a821175f27bc6451883a70e81459"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463787734
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285764, 'matching_hash': 'c4d507dbbdae18b2'}}}